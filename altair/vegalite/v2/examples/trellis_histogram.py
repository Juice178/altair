"""
Trellis Histogram
-----------------
This example shows how to make a basic trellis histogram.
https://vega.github.io/vega-lite/examples/trellis_bar_histogram.html
"""
import altair as alt

cars = alt.load_dataset('cars')

chart = alt.Chart(cars).mark_bar().encode(
    x=alt.X("Horsepower",
            type="quantitative",
            bin=alt.BinTransform(
                maxbins=15
            )),
    y='count(*):Q',
    row='Origin'
)
