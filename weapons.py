import datasets
import pandas as pd
import plotly.express as px
from PIL import Image
import requests
from io import BytesIO

def get_dataset_as_dict():
  return datasets.get_weapons_dataset_as_dict()

def get_dataset_as_dataframe():
  return pd.DataFrame(get_dataset_as_dict())

def get_available_plots():
  return [
    {
      "id": 1,
      "title": "Which Weapon has the Highest Fire Rate?",
      "description": "Below Chart shows Weapons and their Fire Rate's",
      "types": [
        {
          "id": 1,
          "type": "Line Chart",
          "is_default": False
        },
        {
          "id": 2,
          "type": "Bar Chart",
          "is_default": True
        },
        {
          "id": 3,
          "type": "Scatter Chart",
          "is_default": False
        }
      ]
    },
    {
      "id": 2,
      "title": "Which Weapon Category has the Highest Fire Rate?",
      "description": "Below Chart shows Weapon Category with Highest Fire Rate",
      "types": [
        {
          "id": 1,
          "type": "Box Chart",
          "is_default": True
        },
        {
          "id": 2,
          "type": "Bar Chart",
          "is_default": False
        },
        {
          "id": 3,
          "type": "Scatter Chart",
          "is_default": False
        }
      ]
    },
    {
      "id": 3,
      "title": "Which Weapon has the Biggest Magazine?",
      "description": "Below Chart shows Weapons and their Magazine Size",
      "types": [
        {
          "id": 1,
          "type": "Line Chart",
          "is_default": True
        },
        {
          "id": 2,
          "type": "Bar Chart",
          "is_default": False
        },
        {
          "id": 3,
          "type": "Scatter Chart",
          "is_default": False
        }
      ]
    },
    {
      "id": 4,
      "title": "Which Weapon has the Highest Wall Penetration Power?",
      "description": "Below Chart shows Weapons and their Wall Penetration Power",
      "types": [
        {
          "id": 1,
          "type": "Line Chart",
          "is_default": False
        },
        {
          "id": 2,
          "type": "Bar Chart",
          "is_default": False
        },
        {
          "id": 3,
          "type": "Scatter Chart",
          "is_default": True
        }
      ]
    },
    {
      "id": 5,
      "title": "Which Weapon Does the Most Damage?",
      "description": "Below Chart shows Weapons and their Damage",
      "types": [
        {
          "id": 1,
          "type": "Line Chart",
          "is_default": False
        },
        {
          "id": 2,
          "type": "Bar Chart",
          "is_default": True
        },
        {
          "id": 3,
          "type": "Scatter Chart",
          "is_default": False
        }
      ]
    }
  ]

def get_plot(plot_id, plot_type_id):
  if(plot_id == 1):
    return get_weapon_firerate_plot(plot_type_id)
  
  if(plot_id == 2):
    return get_weapon_category_firerate_plot(plot_type_id)
  
  if(plot_id == 3):
    return get_weapon_magazine_plot(plot_type_id)
  
  if(plot_id == 4):
    return get_weapon_wallpenetration_plot(plot_type_id)
  
  if(plot_id == 5):
    return get_weapon_damage_plot(plot_type_id)
  
  return get_weapon_firerate_plot(plot_type_id)

def get_weapon_firerate_plot(plot_type_id=1):
  df = get_dataset_as_dataframe()
  fig = None

  if(plot_type_id == 1):
    fig = px.line(df, x="displayName", y="fireRate", labels={
                     "displayName": "Weapon",
                     "fireRate": "Fire Rate"
                    }, template="plotly_dark")
  if(plot_type_id == 2):
    fig = px.bar(df, x="displayName", y="fireRate", labels={
                     "displayName": "Weapon",
                     "fireRate": "Fire Rate"
                    }, template="plotly_dark")
  if(plot_type_id == 3):
    fig = px.scatter(df, x="displayName", y="fireRate", labels={
                     "displayName": "Weapon",
                     "fireRate": "Fire Rate"
                    }, template="plotly_dark")

  for x in fig.data[0].x:
      response = requests.get(df.loc[df["displayName"] == x]["displayIcon"].values[0])
      img = Image.open(BytesIO(response.content))
      fig.add_layout_image(
        source=img,
        x=x,
        y=1,
        xref="x",
        yref="y",
        xanchor="center",
        sizex=1,
        sizey=1,
      )
      
  return fig.to_html()

def get_weapon_category_firerate_plot(plot_type_id=1):
  df = get_dataset_as_dataframe()
  data = df.groupby("category").agg("median").sort_values(by="fireRate", ascending=False).reset_index()
  fig = None

  if(plot_type_id == 1):
    fig = px.box(data, x="category", y="fireRate", labels={
                     "category": "Weapon Category",
                     "fireRate": "Fire Rate"
                    }, template="plotly_dark")
  if(plot_type_id == 2):
    fig = px.bar(data, x="category", y="fireRate", labels={
                     "category": "Weapon Category",
                     "fireRate": "Fire Rate"
                    }, template="plotly_dark")
  if(plot_type_id == 3):
    fig = px.scatter(data, x="category", y="fireRate", labels={
                     "category": "Weapon Category",
                     "fireRate": "Fire Rate"
                    }, template="plotly_dark")

  for x in fig.data[0].x:
      response = requests.get(df.loc[df["category"] == x]["displayIcon"].values[0])
      img = Image.open(BytesIO(response.content))
      fig.add_layout_image(
        source=img,
        x=x,
        y=1.5,
        xref="x",
        yref="y",
        xanchor="center",
        sizex=1,
        sizey=1,
      )
      
  return fig.to_html()


def get_weapon_magazine_plot(plot_type_id=1):
  df = get_dataset_as_dataframe()
  fig = None

  if(plot_type_id == 1):
    fig = px.line(df, x="displayName", y="magazineSize", labels={
                     "displayName": "Weapon",
                     "magazineSize": "Magazine Size"
                    }, template="plotly_dark")
  if(plot_type_id == 2):
    fig = px.bar(df, x="displayName", y="magazineSize", labels={
                     "displayName": "Weapon",
                     "magazineSize": "Magazine Size"
                    }, template="plotly_dark")
  if(plot_type_id == 3):
    fig = px.scatter(df, x="displayName", y="magazineSize", labels={
                     "displayName": "Weapon",
                     "magazineSize": "Magazine Size"
                    }, template="plotly_dark")

  for x in fig.data[0].x:
      response = requests.get(df.loc[df["displayName"] == x]["displayIcon"].values[0])
      img = Image.open(BytesIO(response.content))
      fig.add_layout_image(
        source=img,
        x=x,
        y=1,
        xref="x",
        yref="y",
        xanchor="center",
        sizex=1,
        sizey=1,
      )
      
  return fig.to_html()

def get_weapon_wallpenetration_plot(plot_type_id=1):
  df = get_dataset_as_dataframe()
  fig = None

  if(plot_type_id == 1):
    fig = px.line(df, x="displayName", y="wallPenetration", labels={
                     "displayName": "Weapon",
                     "wallPenetration": "Wall Penetration Power"
                    }, template="plotly_dark")
  if(plot_type_id == 2):
    fig = px.bar(df, x="displayName", y="wallPenetration", labels={
                     "displayName": "Weapon",
                     "wallPenetration": "Wall Penetration Power"
                    }, template="plotly_dark")
  if(plot_type_id == 3):
    fig = px.scatter(df, x="displayName", y="wallPenetration", labels={
                     "displayName": "Weapon",
                     "wallPenetration": "Wall Penetration Power"
                    }, template="plotly_dark")

  for x in fig.data[0].x:
      response = requests.get(df.loc[df["displayName"] == x]["displayIcon"].values[0])
      img = Image.open(BytesIO(response.content))
      fig.add_layout_image(
        source=img,
        x=x,
        y=0.1,
        xref="x",
        yref="y",
        xanchor="center",
        sizex=1,
        sizey=1,
      )
      
  return fig.to_html()

def get_weapon_damage_plot(plot_type_id=1):
  df = get_dataset_as_dataframe()
  fig = None

  if(plot_type_id == 1):
    fig = px.line(df, x="displayName", y=["headDamage", "bodyDamage", "legDamage"], template="plotly_dark")
  if(plot_type_id == 2):
    fig = px.bar(df, x="displayName", y=["headDamage", "bodyDamage", "legDamage"], template="plotly_dark")
  if(plot_type_id == 3):
    fig = px.scatter(df, x="displayName", y=["headDamage", "bodyDamage", "legDamage"], template="plotly_dark")

  for x in fig.data[0].x:
      response = requests.get(df.loc[df["displayName"] == x]["displayIcon"].values[0])
      img = Image.open(BytesIO(response.content))
      fig.add_layout_image(
        source=img,
        x=x,
        y=1,
        xref="x",
        yref="y",
        xanchor="center",
        sizex=1,
        sizey=1,
      )
      
  fig.update_layout(xaxis_title="Weapon", yaxis_title="Damage", legend_title="Type of Damage")
      
  return fig.to_html()