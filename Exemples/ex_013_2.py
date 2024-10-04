import datetime

weekday = datetime.datetime.today().weekday()
jour_semaine = ""
match weekday:
    case 0:
        jour_semaine = "Lundi"
    case 1:
        jour_semaine = "Mardi"
    case 2:
        jour_semaine = "Mercredi"
    case 3:
        jour_semaine = "Jeudi"
    case 4:
        jour_semaine = "Vendredi"
    case 5:
        jour_semaine = "Samedi"
    case 6:
        jour_semaine = "Dimanche"
print("Le jour de la semaine est", jour_semaine)