import pygame
import pyperclip  # Importer la bibliothèque pyperclip pour le presse-papier

# Initialisation de Pygame
pygame.init()

# Définir les couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)

# Définir la police
font = pygame.font.Font(None, 32)

# Définir les dimensions et la position du bouton
largeur_bouton = 150
hauteur_bouton = 50
position_bouton_x1 = 50
position_bouton_y1 = 100
position_bouton_x2 = 250
position_bouton_y2 = 100
position_bouton_x3 = 450
position_bouton_y3 = 100
position_bouton_x4 = 650
position_bouton_y4 = 100
position_bouton_x5 = 850
position_bouton_y5 = 100
position_bouton_x6 = 1050
position_bouton_y6 = 100
position_bouton_x7 = 1250
position_bouton_y7 = 100
position_bouton_x8 = 1450
position_bouton_y8 = 100
position_bouton_x9 = 50
position_bouton_y9 = 200
position_bouton_x10 = 250
position_bouton_y10 = 200
position_bouton_x11 = 450
position_bouton_y11 = 200
position_bouton_x12 = 650
position_bouton_y12 = 200
position_bouton_x13 = 850
position_bouton_y13 = 200
position_bouton_x14 = 1050
position_bouton_y14 = 200
position_bouton_x15 = 1250
position_bouton_y15 = 200
position_bouton_x16 = 1450
position_bouton_y16 = 200
position_bouton_x17 = 50
position_bouton_y17 = 300
position_bouton_x18 = 250
position_bouton_y18 = 300
position_bouton_x19 = 450
position_bouton_y19 = 300
position_bouton_x20 = 650
position_bouton_y20 = 300
position_bouton_x21 = 850
position_bouton_y21 = 300
position_bouton_x22 = 1050
position_bouton_y22 = 300
position_bouton_x23 = 1250
position_bouton_y23 = 300
position_bouton_x24 = 1450
position_bouton_y24 = 300

# Textes à copier dans le presse-papiers première ligne
texte_a_copier1 = "Text"
texte_a_copier2 = "Text"
texte_a_copier3 = "Text"
texte_a_copier4 = "Text"
texte_a_copier5 = "Text"
texte_a_copier6 = "Text"
texte_a_copier7 = "Text"
texte_a_copier8 = "Text"
# Textes à copier dans le presse-papiers deuxième ligne
texte_a_copier9 = "Text"
texte_a_copier10 = "Text"
texte_a_copier11 = "Text"
texte_a_copier12 = "Text"
texte_a_copier13 = "Text"
texte_a_copier14 = "Text"
texte_a_copier15 = "Text"
texte_a_copier16 = "Text"
# Textes à copier dans le presse-papiers troisième ligne
texte_a_copier17 = "Text"
texte_a_copier18 = "Text"
texte_a_copier19 = "Text"
texte_a_copier20 = "Text"
texte_a_copier21 = "Text"
texte_a_copier22 = "Text"
texte_a_copier23 = "Text"
texte_a_copier24 = "Text"


# Créer la surface de l'écran
ecran = pygame.display.set_mode((1650, 400))
pygame.display.set_caption("Bouton Copier Pygame")

# Boucle principale
continuer = True
while continuer:
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        # Détecter le clic de la souris sur le bouton
        if event.type == pygame.MOUSEBUTTONDOWN:
            clic_souris_x, clic_souris_y = event.pos
## Première ligne
            if clic_souris_x >= position_bouton_x1 and clic_souris_x <= position_bouton_x1 + largeur_bouton and clic_souris_y >= position_bouton_y1 and clic_souris_y <= position_bouton_y1 + hauteur_bouton:
                # Copier le texte dans le presse-papiers
                pyperclip.copy(texte_a_copier1)
                print("Texte copié dans le presse-papiers !")
            elif clic_souris_x >= position_bouton_x2 and clic_souris_x <= position_bouton_x2 + largeur_bouton and clic_souris_y >= position_bouton_y2 and clic_souris_y <= position_bouton_y2 + hauteur_bouton:
                # Copier le texte dans le presse-papiers
                pyperclip.copy(texte_a_copier2)
                print("Texte copié dans le presse-papiers !")     
            elif clic_souris_x >= position_bouton_x3 and clic_souris_x <= position_bouton_x3 + largeur_bouton and clic_souris_y >= position_bouton_y3 and clic_souris_y <= position_bouton_y3 + hauteur_bouton:
                # Copier le texte dans le presse-papiers
                pyperclip.copy(texte_a_copier3)
                print("Texte copié dans le presse-papiers !")   
            elif clic_souris_x >= position_bouton_x4 and clic_souris_x <= position_bouton_x4 + largeur_bouton and clic_souris_y >= position_bouton_y4 and clic_souris_y <= position_bouton_y4 + hauteur_bouton:
                # Copier le texte dans le presse-papiers
                pyperclip.copy(texte_a_copier4)
                print("Texte copié dans le presse-papiers !")   
            elif clic_souris_x >= position_bouton_x5 and clic_souris_x <= position_bouton_x5 + largeur_bouton and clic_souris_y >= position_bouton_y5 and clic_souris_y <= position_bouton_y5 + hauteur_bouton:
                # Copier le texte dans le presse-papiers
                pyperclip.copy(texte_a_copier5)
                print("Texte copié dans le presse-papiers !")   
            elif clic_souris_x >= position_bouton_x6 and clic_souris_x <= position_bouton_x6 + largeur_bouton and clic_souris_y >= position_bouton_y6 and clic_souris_y <= position_bouton_y6 + hauteur_bouton:
                # Copier le texte dans le presse-papiers
                pyperclip.copy(texte_a_copier6)
                print("Texte copié dans le presse-papiers !")   
            elif clic_souris_x >= position_bouton_x7 and clic_souris_x <= position_bouton_x7 + largeur_bouton and clic_souris_y >= position_bouton_y7 and clic_souris_y <= position_bouton_y7 + hauteur_bouton:
                # Copier le texte dans le presse-papiers
                pyperclip.copy(texte_a_copier7)
                print("Texte copié dans le presse-papiers !")
            elif clic_souris_x >= position_bouton_x8 and clic_souris_x <= position_bouton_x8 + largeur_bouton and clic_souris_y >= position_bouton_y8 and clic_souris_y <= position_bouton_y8 + hauteur_bouton:
                # Copier le texte dans le presse-papiers
                pyperclip.copy(texte_a_copier8)
                print("Texte copié dans le presse-papiers !")
##Deuxième ligne
            elif clic_souris_x >= position_bouton_x9 and clic_souris_x <= position_bouton_x9 + largeur_bouton and clic_souris_y >= position_bouton_y9 and clic_souris_y <= position_bouton_y9 + hauteur_bouton:
                # Copier le texte dans le presse-papiers
                pyperclip.copy(texte_a_copier9)
                print("Texte copié dans le presse-papiers !")
            elif clic_souris_x >= position_bouton_x10 and clic_souris_x <= position_bouton_x10 + largeur_bouton and clic_souris_y >= position_bouton_y10 and clic_souris_y <= position_bouton_y10 + hauteur_bouton:
                # Copier le texte dans le presse-papiers
                pyperclip.copy(texte_a_copier10)
                print("Texte copié dans le presse-papiers !")     
            elif clic_souris_x >= position_bouton_x11 and clic_souris_x <= position_bouton_x11 + largeur_bouton and clic_souris_y >= position_bouton_y11 and clic_souris_y <= position_bouton_y11 + hauteur_bouton:
                # Copier le texte dans le presse-papiers
                pyperclip.copy(texte_a_copier11)
                print("Texte copié dans le presse-papiers !")   
            elif clic_souris_x >= position_bouton_x12 and clic_souris_x <= position_bouton_x12 + largeur_bouton and clic_souris_y >= position_bouton_y12 and clic_souris_y <= position_bouton_y12 + hauteur_bouton:
                # Copier le texte dans le presse-papiers
                pyperclip.copy(texte_a_copier12)
                print("Texte copié dans le presse-papiers !")   
            elif clic_souris_x >= position_bouton_x13 and clic_souris_x <= position_bouton_x13 + largeur_bouton and clic_souris_y >= position_bouton_y13 and clic_souris_y <= position_bouton_y13 + hauteur_bouton:
                # Copier le texte dans le presse-papiers
                pyperclip.copy(texte_a_copier13)
                print("Texte copié dans le presse-papiers !")   
            elif clic_souris_x >= position_bouton_x14 and clic_souris_x <= position_bouton_x14 + largeur_bouton and clic_souris_y >= position_bouton_y14 and clic_souris_y <= position_bouton_y14 + hauteur_bouton:
                # Copier le texte dans le presse-papiers
                pyperclip.copy(texte_a_copier14)
                print("Texte copié dans le presse-papiers !")   
            elif clic_souris_x >= position_bouton_x15 and clic_souris_x <= position_bouton_x15 + largeur_bouton and clic_souris_y >= position_bouton_y15 and clic_souris_y <= position_bouton_y15 + hauteur_bouton:
                # Copier le texte dans le presse-papiers
                pyperclip.copy(texte_a_copier15)
                print("Texte copié dans le presse-papiers !")
            elif clic_souris_x >= position_bouton_x16 and clic_souris_x <= position_bouton_x16 + largeur_bouton and clic_souris_y >= position_bouton_y16 and clic_souris_y <= position_bouton_y16 + hauteur_bouton:
                # Copier le texte dans le presse-papiers
                pyperclip.copy(texte_a_copier16)
                print("Texte copié dans le presse-papiers !")
##Troisième ligne
            elif clic_souris_x >= position_bouton_x17 and clic_souris_x <= position_bouton_x17 + largeur_bouton and clic_souris_y >= position_bouton_y17 and clic_souris_y <= position_bouton_y17 + hauteur_bouton:
                # Copier le texte dans le presse-papiers
                pyperclip.copy(texte_a_copier17)
                print("Texte copié dans le presse-papiers !")
            elif clic_souris_x >= position_bouton_x18 and clic_souris_x <= position_bouton_x18 + largeur_bouton and clic_souris_y >= position_bouton_y18 and clic_souris_y <= position_bouton_y18 + hauteur_bouton:
                # Copier le texte dans le presse-papiers
                pyperclip.copy(texte_a_copier18)
                print("Texte copié dans le presse-papiers !")     
            elif clic_souris_x >= position_bouton_x19 and clic_souris_x <= position_bouton_x19 + largeur_bouton and clic_souris_y >= position_bouton_y19 and clic_souris_y <= position_bouton_y19 + hauteur_bouton:
                # Copier le texte dans le presse-papiers
                pyperclip.copy(texte_a_copier19)
                print("Texte copié dans le presse-papiers !")   
            elif clic_souris_x >= position_bouton_x20 and clic_souris_x <= position_bouton_x20 + largeur_bouton and clic_souris_y >= position_bouton_y20 and clic_souris_y <= position_bouton_y20 + hauteur_bouton:
                # Copier le texte dans le presse-papiers
                pyperclip.copy(texte_a_copier20)
                print("Texte copié dans le presse-papiers !")   
            elif clic_souris_x >= position_bouton_x21 and clic_souris_x <= position_bouton_x21 + largeur_bouton and clic_souris_y >= position_bouton_y21 and clic_souris_y <= position_bouton_y21 + hauteur_bouton:
                # Copier le texte dans le presse-papiers
                pyperclip.copy(texte_a_copier21)
                print("Texte copié dans le presse-papiers !")   
            elif clic_souris_x >= position_bouton_x22 and clic_souris_x <= position_bouton_x22 + largeur_bouton and clic_souris_y >= position_bouton_y22 and clic_souris_y <= position_bouton_y22 + hauteur_bouton:
                # Copier le texte dans le presse-papiers
                pyperclip.copy(texte_a_copier22)
                print("Texte copié dans le presse-papiers !")   
            elif clic_souris_x >= position_bouton_x23 and clic_souris_x <= position_bouton_x23 + largeur_bouton and clic_souris_y >= position_bouton_y23 and clic_souris_y <= position_bouton_y23 + hauteur_bouton:
                # Copier le texte dans le presse-papiers
                pyperclip.copy(texte_a_copier23)
                print("Texte copié dans le presse-papiers !")
            elif clic_souris_x >= position_bouton_x24 and clic_souris_x <= position_bouton_x24 + largeur_bouton and clic_souris_y >= position_bouton_y24 and clic_souris_y <= position_bouton_y24 + hauteur_bouton:
                # Copier le texte dans le presse-papiers
                pyperclip.copy(texte_a_copier24)
                print("Texte copié dans le presse-papiers !")                

    # Remplir l'écran de noir
    ecran.fill(NOIR)

    # Dessiner le bouton
    bouton_rect1 = pygame.Rect(position_bouton_x1, position_bouton_y1, largeur_bouton, hauteur_bouton)
    bouton_rect2 = pygame.Rect(position_bouton_x2, position_bouton_y2, largeur_bouton, hauteur_bouton)
    bouton_rect3 = pygame.Rect(position_bouton_x3, position_bouton_y3, largeur_bouton, hauteur_bouton)
    bouton_rect4 = pygame.Rect(position_bouton_x4, position_bouton_y4, largeur_bouton, hauteur_bouton)
    bouton_rect5 = pygame.Rect(position_bouton_x5, position_bouton_y5, largeur_bouton, hauteur_bouton)
    bouton_rect6 = pygame.Rect(position_bouton_x6, position_bouton_y6, largeur_bouton, hauteur_bouton)
    bouton_rect7 = pygame.Rect(position_bouton_x7, position_bouton_y7, largeur_bouton, hauteur_bouton)
    bouton_rect8 = pygame.Rect(position_bouton_x8, position_bouton_y8, largeur_bouton, hauteur_bouton)
    
    bouton_rect9 = pygame.Rect(position_bouton_x9, position_bouton_y9, largeur_bouton, hauteur_bouton)
    bouton_rect10 = pygame.Rect(position_bouton_x10, position_bouton_y10, largeur_bouton, hauteur_bouton)
    bouton_rect11 = pygame.Rect(position_bouton_x11, position_bouton_y11, largeur_bouton, hauteur_bouton)
    bouton_rect12 = pygame.Rect(position_bouton_x12, position_bouton_y12, largeur_bouton, hauteur_bouton)
    bouton_rect13 = pygame.Rect(position_bouton_x13, position_bouton_y13, largeur_bouton, hauteur_bouton)
    bouton_rect14 = pygame.Rect(position_bouton_x14, position_bouton_y14, largeur_bouton, hauteur_bouton)
    bouton_rect15 = pygame.Rect(position_bouton_x15, position_bouton_y15, largeur_bouton, hauteur_bouton)
    bouton_rect16 = pygame.Rect(position_bouton_x16, position_bouton_y16, largeur_bouton, hauteur_bouton)
    
    bouton_rect17 = pygame.Rect(position_bouton_x17, position_bouton_y17, largeur_bouton, hauteur_bouton)
    bouton_rect18 = pygame.Rect(position_bouton_x18, position_bouton_y18, largeur_bouton, hauteur_bouton)
    bouton_rect19 = pygame.Rect(position_bouton_x19, position_bouton_y19, largeur_bouton, hauteur_bouton)
    bouton_rect20 = pygame.Rect(position_bouton_x20, position_bouton_y20, largeur_bouton, hauteur_bouton)
    bouton_rect21 = pygame.Rect(position_bouton_x21, position_bouton_y21, largeur_bouton, hauteur_bouton)
    bouton_rect22 = pygame.Rect(position_bouton_x22, position_bouton_y22, largeur_bouton, hauteur_bouton)
    bouton_rect23 = pygame.Rect(position_bouton_x23, position_bouton_y23, largeur_bouton, hauteur_bouton)
    bouton_rect24 = pygame.Rect(position_bouton_x24, position_bouton_y24, largeur_bouton, hauteur_bouton)
    
    pygame.draw.rect(ecran, ROUGE, bouton_rect1)
    pygame.draw.rect(ecran, ROUGE, bouton_rect2)
    pygame.draw.rect(ecran, ROUGE, bouton_rect3)
    pygame.draw.rect(ecran, ROUGE, bouton_rect4)
    pygame.draw.rect(ecran, ROUGE, bouton_rect5)
    pygame.draw.rect(ecran, ROUGE, bouton_rect6)
    pygame.draw.rect(ecran, ROUGE, bouton_rect7)
    pygame.draw.rect(ecran, ROUGE, bouton_rect8)
       
    pygame.draw.rect(ecran, ROUGE, bouton_rect9)
    pygame.draw.rect(ecran, ROUGE, bouton_rect10)
    pygame.draw.rect(ecran, ROUGE, bouton_rect11)
    pygame.draw.rect(ecran, ROUGE, bouton_rect12)
    pygame.draw.rect(ecran, ROUGE, bouton_rect13)
    pygame.draw.rect(ecran, ROUGE, bouton_rect14)
    pygame.draw.rect(ecran, ROUGE, bouton_rect15)
    pygame.draw.rect(ecran, ROUGE, bouton_rect16)

    pygame.draw.rect(ecran, ROUGE, bouton_rect17)
    pygame.draw.rect(ecran, ROUGE, bouton_rect18)
    pygame.draw.rect(ecran, ROUGE, bouton_rect19)
    pygame.draw.rect(ecran, ROUGE, bouton_rect20)
    pygame.draw.rect(ecran, ROUGE, bouton_rect21)
    pygame.draw.rect(ecran, ROUGE, bouton_rect22)
    pygame.draw.rect(ecran, ROUGE, bouton_rect23)
    pygame.draw.rect(ecran, ROUGE, bouton_rect24)

    # Dessiner le texte du bouton
    texte_bouton = font.render("Text", True, BLANC)
    texte_rect = texte_bouton.get_rect(center=bouton_rect1.center)
    ecran.blit(texte_bouton, texte_rect)
    texte_bouton = font.render("Text ", True, BLANC)
    texte_rect = texte_bouton.get_rect(center=bouton_rect2.center)
    ecran.blit(texte_bouton, texte_rect)
    texte_bouton = font.render("Text", True, BLANC)
    texte_rect = texte_bouton.get_rect(center=bouton_rect3.center)
    ecran.blit(texte_bouton, texte_rect)
    texte_bouton = font.render("Text", True, BLANC)
    texte_rect = texte_bouton.get_rect(center=bouton_rect4.center)
    ecran.blit(texte_bouton, texte_rect)
    texte_bouton = font.render("Text", True, BLANC)
    texte_rect = texte_bouton.get_rect(center=bouton_rect5.center)
    ecran.blit(texte_bouton, texte_rect)
    texte_bouton = font.render("Text", True, BLANC)
    texte_rect = texte_bouton.get_rect(center=bouton_rect6.center)
    ecran.blit(texte_bouton, texte_rect)
    texte_bouton = font.render("Text", True, BLANC)
    texte_rect = texte_bouton.get_rect(center=bouton_rect7.center)
    ecran.blit(texte_bouton, texte_rect)
    texte_bouton = font.render("Text", True, BLANC)
    texte_rect = texte_bouton.get_rect(center=bouton_rect8.center)
    ecran.blit(texte_bouton, texte_rect)

    texte_bouton = font.render("Text", True, BLANC)
    texte_rect = texte_bouton.get_rect(center=bouton_rect9.center)
    ecran.blit(texte_bouton, texte_rect)
    texte_bouton = font.render("Text", True, BLANC)
    texte_rect = texte_bouton.get_rect(center=bouton_rect10.center)
    ecran.blit(texte_bouton, texte_rect)
    texte_bouton = font.render("Text", True, BLANC)
    texte_rect = texte_bouton.get_rect(center=bouton_rect11.center)
    ecran.blit(texte_bouton, texte_rect)
    texte_bouton = font.render("Text", True, BLANC)
    texte_rect = texte_bouton.get_rect(center=bouton_rect12.center)
    ecran.blit(texte_bouton, texte_rect)
    texte_bouton = font.render("Text", True, BLANC)
    texte_rect = texte_bouton.get_rect(center=bouton_rect13.center)
    ecran.blit(texte_bouton, texte_rect)
    texte_bouton = font.render("Text", True, BLANC)
    texte_rect = texte_bouton.get_rect(center=bouton_rect14.center)
    ecran.blit(texte_bouton, texte_rect)
    texte_bouton = font.render("Text", True, BLANC)
    texte_rect = texte_bouton.get_rect(center=bouton_rect15.center)
    ecran.blit(texte_bouton, texte_rect)
    texte_bouton = font.render("Text", True, BLANC)
    texte_rect = texte_bouton.get_rect(center=bouton_rect16.center)
    ecran.blit(texte_bouton, texte_rect)

    texte_bouton = font.render("Text", True, BLANC)
    texte_rect = texte_bouton.get_rect(center=bouton_rect17.center)
    ecran.blit(texte_bouton, texte_rect)
    texte_bouton = font.render("Text", True, BLANC)
    texte_rect = texte_bouton.get_rect(center=bouton_rect18.center)
    ecran.blit(texte_bouton, texte_rect)
    texte_bouton = font.render("Text", True, BLANC)
    texte_rect = texte_bouton.get_rect(center=bouton_rect19.center)
    ecran.blit(texte_bouton, texte_rect)
    texte_bouton = font.render("Text", True, BLANC)
    texte_rect = texte_bouton.get_rect(center=bouton_rect20.center)
    ecran.blit(texte_bouton, texte_rect)
    texte_bouton = font.render("Text", True, BLANC)
    texte_rect = texte_bouton.get_rect(center=bouton_rect21.center)
    ecran.blit(texte_bouton, texte_rect)
    texte_bouton = font.render("Text ", True, BLANC)
    texte_rect = texte_bouton.get_rect(center=bouton_rect22.center)
    ecran.blit(texte_bouton, texte_rect)
    texte_bouton = font.render("Text", True, BLANC)
    texte_rect = texte_bouton.get_rect(center=bouton_rect23.center)
    ecran.blit(texte_bouton, texte_rect)
    texte_bouton = font.render("Text", True, BLANC)
    texte_rect = texte_bouton.get_rect(center=bouton_rect24.center)
    ecran.blit(texte_bouton, texte_rect)

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
