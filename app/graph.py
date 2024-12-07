from altair import Chart
from .data import Database
import altair as alt


def chart(df, x: str, y: str, target: str) -> Chart:

    db = Database()
    df = db.dataframe()


    if df.empty:
        print("Connection could not be established")
        return None

    chart_title= f'{y} and {x} for {target}'

    missing_columns = [col for col in [x, y, target] if col not in df.columns]
    if missing_columns:
        raise ValueError(f"the following are missing in the DataFrame")

    graph = alt.Chart(df).mark_circle(size=100, stroke='black', strokeWidth=2).encode(
      x= alt.X(x, title=x),
      y= alt.Y(y, title=y),
      color = alt.Color(target, title=target),
      tooltip=[x, y, target]
    ).properties(
        title=chart_title,
        width=600,
        height=600
    )


    graph = graph.configure_view(
        stroke=None
    ).configure(background='black'
                ).configure_axis(
        labelColor='white',
        titleColor='white'
    ).configure_title(
        fontSize=30,
        color='white',
        anchor='middle'
    ).configure_legend(
        labelColor='white',
        titleColor='white'
    )

    return graph
