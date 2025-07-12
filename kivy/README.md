# Kivy Examples

This folder contains beginner-friendly examples using the Kivy framework for building cross-platform GUI applications in Python. Each example demonstrates different aspects of Kivy layouts, widgets, and design language (`.kv` files).

## Requirements

Before running these examples, make sure you have Kivy installed in your virtual environment. You can find instructions at https://kivy.org/

## File Overview

### 1. hello_world.py
A simple "Hello, World!" label in a Kivy app using the Label widget.

### 2. input.py
Demonstrates TextInput, Button, and layout composition using GridLayout. User inputs are printed and reset.

### 3. design.py + design.kv
Separates layout into a .kv file for better organization. Demonstrates ObjectProperty binding to TextInput.

### 4. color.py + color.kv
Shows how to style buttons using both RGBA tuples and hex color codes.

### 5. box_layout.py + box_layout.kv
Demonstrates button alignment and layout spacing using BoxLayout.

### 6. inherit.py + inherit.kv
Demonstrates how to style all Button widgets at once using class-level rules. Includes layout with inputs and buttons.

### 7. label_color.py + label_color.kv
Customizes Label appearance using canvas.before to draw a background and apply styles like bold, italic, and outline.

### 8. bg.py + bg.kv
Demonstrates adding a background color and an Image widget to a BoxLayout.

### 9. float_layout.py + float_layout.kv
Demonstrates absolute positioning using FloatLayout and pos_hint for flexible UI design.

### 10. update_label.py + update_label.kv
Updates a label with the user's input from a TextInput using ids and method binding.

## Notes
Kivy automatically loads a .kv file with the same name as the App class, minus the App suffix and in lowercase (e.g., ColorApp → color.kv).

You can also manually load the .kv file using Builder.load_file(...).