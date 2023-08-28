import streamlit as st
import pandas as pd
import altair as alt

st.header("Welche Reaktionen ruft Schulstress bei Ihrem eigenen Kind hervor?")
st.subheader("")

source = pd.DataFrame({
        'Anteil(%)': [57, 50, 43, 42, 32, 29, 14],
        'Reaktion': ['Unkonzentriertheit', 'Kopf-Bauchschmerzen', 'Traurigkeit', 'Aggressionen', 'Lern-Leistungsstörungen', 'Unwille zur Schule zu gehen', 'Häufiges krank sein']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Reaktion:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis: 651; Deutschland Eltern von Schulkind unter 18 Jahren 
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle:  forsa")