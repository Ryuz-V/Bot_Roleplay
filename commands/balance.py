import discord
from discord import app_commands
import json
import os

DATA_FILE = "carrot.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app_commands.command(
    name="balance",
    description="Check your carrot balance"
)
async def balance(interaction: discord.Interaction):
    data = load_data()
    user_id = str(interaction.user.id)

    if user_id not in data:
        data[user_id] = 1000
        save_data(data)

    await interaction.response.send_message(
        f"🥕 Carrot kamu: **{data[user_id]}**",
        ephemeral=True
    )
