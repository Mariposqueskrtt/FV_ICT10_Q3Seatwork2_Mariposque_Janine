from pyscript import display, document

def intrams_checker(event=None):
    # Get selected radio buttons
    registration_el = document.querySelector('input[name="registration"]:checked')
    medical_el = document.querySelector('input[name="clearance"]:checked')

    grade_level = document.getElementById("grade_level").value
    section = document.getElementById("section").value

    # Validation
    if registration_el is None or medical_el is None:
        display("Please answer all yes/no questions.", target="result")
        return

    registration = registration_el.value
    medical = medical_el.value

    # Team assignment
    teams = {
        "Emerald": "Red Bulldogs",
        "Ruby": "Blue Bears",
        "Sapphire": "Green Hornets",
        "Topaz": "Yellow Tigers",
    }

    if registration == "yes" and medical == "yes" and grade_level in ["grade7", "grade8", "grade9", "grade10"]:
        team = teams.get(section, "No team assigned")
        display(f"You are eligible! You are in {team}.", target="result")
