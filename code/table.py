import pandas as pd

df = pd.DataFrame(
    dict(name=['Frederico', 'Donatello'],
    age=[24, 45],
    height=[170.85, 177.65]))

df.to_latex(
    "./src/tables/people.tex",
    index=False,
    formatters={"name": str.upper},
    float_format="{:.1f}".format,
)