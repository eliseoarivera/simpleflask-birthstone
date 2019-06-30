birthstone = {
  "january": "Garnet",
  "february": "Amethyst",
  "march": "Aquamarine",
  "april": "Diamond",
  "may": "Emerald",
  "june": "Pearl",
  "july": "Ruby",
  "august": "Peridot",
  "september": "Sapphire",
  "october": "Opal",
  "november": "Topaz",
  "december": "Turquoise"
}
# need to take the users "birthMonth" and return back birthstone

def birthStone(month):
  if month.lower() == "january":
    return(birthstone["january"])
  elif month.lower() == "february":
    return(birthstone["february"])
  elif month.lower() == "march":
    return(birthstone["march"])
  elif month.lower() == "april":
    return(birthstone["april"])
  elif month.lower() == "may":
    return(birthstone["may"])
  elif month.lower() == "june":
    return(birthstone["june"])
  elif month.lower() == "july":
    return(birthstone["july"])
  elif month.lower() == "august":
    return(birthstone["august"])
  elif month.lower() == "september":
    return(birthstone["september"])
  elif month.lower() == "october":
    return(birthstone["october"])
  elif month.lower() == "november":
    return(birthstone["november"])
  elif month.lower() == "december":
    return(birthstone["december"])  
  else:
    return "not found. Please type in your birth month"
    
    
"""def shout(word):
    return word.upper()"""