import gradio as gr

# --- Simulation Function ---
def simulate_regen_impact_by_land_share(land_share_converted, total_biscuit_tonnes, current_yield_production):
    price_biscuit = 0.33
    wheat_ratio = 0.5
    wheat_price = 239
    alan_yield = 5.4
    margin = 0.001
    regen_adoption_pct = land_share_converted

    wheat_tonnes = round(total_biscuit_tonnes * wheat_ratio)
    rg_yield = alan_yield * (1 - margin)
    regen_wheat_tonnes = wheat_tonnes * regen_adoption_pct

    yield_gain_pct = (rg_yield -  current_yield_production) /  current_yield_production
    value_gain = regen_wheat_tonnes * yield_gain_pct * wheat_price

    return (
        f"🌾 Yield gain: {round(yield_gain_pct * 100, 2)}%",
        f"💶 Value gain: €{round(value_gain, 2):,}"
    )

# --- Gradio Interface ---
demo = gr.Interface(
    fn=simulate_regen_impact_by_land_share,
    inputs=[
        gr.Slider(0, 1, value=0.25, label="🔄 % of wheat sourced regeneratively"),
        gr.Number(value=250000, label="🏭 Total biscuit production (tonnes/year)"),
        gr.Number(value=6.5, label="🌾 Current yield production (tonnes/ha)")
    ],
    outputs=[
        gr.Textbox(label="📈 Yield Gain"),
        gr.Textbox(label="💰 Value Gain (€)")

    ],
    title=" 🌱 Regenerative Agriculture Simulator",
    description="Estimate the benefits of switching part of your wheat supply to regenerative practices."
)

# --- Launch App ---
demo.launch()
