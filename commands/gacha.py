import discord
from discord import app_commands
import random

from utils.storage import load_data, save_data, GACHA_PRICE, START_CARROT

@app_commands.command(
    name="gacha",
    description="Gacha Umamusume"
)
async def gacha(interaction: discord.Interaction):
    data = load_data()
    user_id = str(interaction.user.id)

    if user_id not in data:
        data[user_id] = START_CARROT

    if data[user_id] < GACHA_PRICE:
        await interaction.response.send_message(
            "❌ You don't have enough carrots!",
            ephemeral=True
        )
        return

    # potong carrot
    data[user_id] -= GACHA_PRICE

    REWARDS = {
        "Common": {
            "chance": 60,
            "items": [
                "Haru Urara", "Winning Ticket", "Air Grove", "Grass Wonder",
                "Sakura Bakushin O", "Shinko Windy", "Super Creek",
                "Bamboo Memory", "Biko Pegasus", "Twin Turbo"
            ]
        },
        "Rare": {
            "chance": 30,
            "items": [
                "Daiwa Scarlet", "Vodka", "El Condor Pasa", "Gold Ship",
                "Yukino Bijin", "Ines Fujin", "Sweep Tosho", "Smart Falcon",
                "Nishino Flower", "Matikanefukukitaru", "Nice Nature",
                "King Halo"
            ]
        },
        "Epic": {
            "chance": 8,
            "items": [
                "Special Week", "Fine Motion", "Biwa Hayahide", "Mejiro Ryan",
                "Hishi Akebono", "Agnes Tachyon", "Air Shakur",
                "Kawakami Princess", "Zenno Rob Roy", "Tosen Jordan",
                "Ikuno Dictus", "Daitaku Helios", "Mejiro Ardan"
            ]
        },
        "Legendary": {
            "chance": 2,
            "items": [
                "Silence Suzuka", "Tokai Teio", "Oguri Cap", "Rice Shower",
                "Maruzensky", "Fuji Kiseki", "Taiki Shuttle", "Hishi Amazon",
                "Mejiro McQueen", "T.M. Opera O", "Narita Brian",
                "Symboli Rudolf", "Agnes Digital", "Seiun Sky",
                "Tamamo Cross", "Mayano Top Gun", "Manhattan Cafe",
                "Mihono Bourbon", "Eishin Flash", "Curren Chan",
                "Gold City", "Seeking The Pearl", "Nakayama Festa",
                "Narita Taishin", "Marvelous Sunday", "Meisho Doto",
                "Mejiro Dober", "Matikanetannhauser", "Mejiro Palmer",
                "Satono Diamond", "Kitasan Black", "Sakura Chiyono O",
                "Sirius Symboli", "Yaeno Muteki"
            ]
        }
    }

    categories = list(REWARDS.keys())
    chances = [REWARDS[c]["chance"] for c in categories]

    chosen_category = random.choices(categories, weights=chances, k=1)[0]
    character = random.choice(REWARDS[chosen_category]["items"])

    save_data(data)

    await interaction.response.send_message(
        f"🎰 **HASIL GACHA** 🎰\n"
        f"Kategori: **{chosen_category}**\n"
        f"Karakter: **{character}**\n"
        f"Sisa carrot: **{data[user_id]}** 🥕"
    )
