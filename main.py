import os
import RLPy
import random
import json
from btp import qt

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))
icons_dir = os.path.join(script_dir, "icons")  # Set the icons directory

# Function to randomize morphs
def randomize_morphs(avatar, morph_targets, category):
    shaping_component = avatar.GetAvatarShapingComponent()
    if shaping_component:
        morph_ids = shaping_component.GetShapingMorphIDs(category)
        display_names = shaping_component.GetShapingMorphDisplayNames(category)
        for i, morph_id in enumerate(morph_ids):
            display_name = display_names[i]
            if display_name in morph_targets:
                min_value, max_value = morph_targets[display_name]
                random_value = random.uniform(min_value, max_value)
                shaping_component.SetShapingMorphWeight(morph_id, random_value)

# Function to load morph data from JSON
def load_morph_data(filename):
    try:
        filepath = os.path.join(script_dir, filename)  # Get full path to the file
        with open(filepath, 'r') as file:
            morph_data = json.load(file)
        return morph_data
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return {}

# Function to get the avatar in the scene
def get_avatar():
    avatars = RLPy.RScene.GetAvatars()
    if avatars:
        return avatars[0]
    else:
        print("No avatars found.")
        return None

# Randomization functions for each button
def menu_randomize_female_head_morphs():
    avatar = get_avatar()
    if avatar:
        morph_targets = load_morph_data("head_morphs.json")
        randomize_morphs(avatar, morph_targets, "Actor/Head")
    print("Female Head randomization executed!")

def menu_randomize_female_body_morphs():
    avatar = get_avatar()
    if avatar:
        morph_targets = load_morph_data("body_morphs.json")
        randomize_morphs(avatar, morph_targets, "Actor/Body")
    print("Female Body randomization executed!")

def menu_randomize_male_head_morphs():
    avatar = get_avatar()
    if avatar:
        morph_targets = load_morph_data("male_head_morphs.json")
        randomize_morphs(avatar, morph_targets, "Actor/Head")
    print("Male Head randomization executed!")

def menu_randomize_male_body_morphs():
    avatar = get_avatar()
    if avatar:
        morph_targets = load_morph_data("male_body_morphs.json")
        randomize_morphs(avatar, morph_targets, "Actor/Body")
    print("Male Body randomization executed!")

# Initialize the plugin and add menu and toolbar actions
def initialize_plugin():
    # Add the "Randomize" buttons under the Plugins menu
    plugin_menu = qt.find_add_plugin_menu("Random Morphs")
    qt.clear_menu(plugin_menu)
    
    # Add the menu actions for female head and body
    qt.add_menu_action(plugin_menu, "Randomize Female Head Morphs", menu_randomize_female_head_morphs)
    qt.add_menu_action(plugin_menu, "Randomize Female Body Morphs", menu_randomize_female_body_morphs)

    # Add the menu actions for male head and body
    qt.add_menu_action(plugin_menu, "Randomize Male Head Morphs", menu_randomize_male_head_morphs)
    qt.add_menu_action(plugin_menu, "Randomize Male Body Morphs", menu_randomize_male_body_morphs)

    # Toolbar
    toolbar = qt.find_add_toolbar("Random Morphs Toolbar")
    qt.clear_toolbar(toolbar)

    # Add toolbar icons
    icon_female_head = qt.get_icon(os.path.join(icons_dir, "female_head_icon.png"))
    qt.add_toolbar_action(toolbar, icon_female_head, "Randomize Female Head Morphs", menu_randomize_female_head_morphs)

    icon_female_body = qt.get_icon(os.path.join(icons_dir, "female_body_icon.png"))
    qt.add_toolbar_action(toolbar, icon_female_body, "Randomize Female Body Morphs", menu_randomize_female_body_morphs)

    icon_male_head = qt.get_icon(os.path.join(icons_dir, "male_head_icon.png"))
    qt.add_toolbar_action(toolbar, icon_male_head, "Randomize Male Head Morphs", menu_randomize_male_head_morphs)

    icon_male_body = qt.get_icon(os.path.join(icons_dir, "male_body_icon.png"))
    qt.add_toolbar_action(toolbar, icon_male_body, "Randomize Male Body Morphs", menu_randomize_male_body_morphs)

# Register the plugin
initialize_plugin()
