
# ScheduleWebApp-Withcmd

## Objectif
Créer une application web de planification d’emploi du temps, couplée à un script Python local, pour organiser et automatiser des actions (lancement d’applis, lecture audio, ouverture de vidéos YouTube) directement depuis l’interface.

---

## Fonctionnement global

1. **`index.html`**  
   - **Interface** : emploi du temps interactif (5 jours × 12 heures).  
   - **Interactions** :  
     - Clic sur une case → ajout de tâche (titre, description, type, données, couleur).  
     - Glisser-déposer pour déplacer les tâches.  
     - Double‑clic ou clic selon le type pour exécuter l’action.  
   - **Types de tâche** : texte, audio, YouTube, application.  
   - **Appel réseau** :  
     - Pour les tâches de type **Application**, un  
       `fetch('http://localhost:5005/run', …)`  
       envoie la commande au serveur local.

2. **`agent.py`**  
   - **Serveur Flask** sur `localhost:5005`, CORS activé.  
   - **Route `/run`** (POST JSON `{ cmd: '...' }`) :  
     - Exécute la commande système (`subprocess.Popen(cmd, shell=True)`).  
     - Retourne `{ status: 'ok' }` ou `{ status: 'error', message: '...' }`.

3. **`python -m http.server 8000`**  
   - Sert le dossier contenant `index.html` pour tester via  
     `http://localhost:8000`.

4. **Flux global**  
   ```text
   Navigateur (index.html)
       ↓ fetch POST → http://localhost:5005/run
   agent.py (Flask)
       ↓ subprocess.Popen(cmd)
   Système Windows 
---
## Explications:
index.html propose de créer des tâches:
- Texte (pur texte)
- Musique (saisir un url et il le lit en arrière plan quand clic sur l'évènement)
- Youtube (ouvre un url du site web Youtube.com)
- <p>Application: Potentiel énorme puisqu'on peut tout faire:
      ↓
  On peut ouvrir cmd et ainsi utiliser curl pour télécharger des scripts, des applis...
  On peut ouvrir n'importe quelle appli existante
  On peut éxécuter n'importe quelle commande, y compris runas qui ouvrira l'uac et donnera le contrôle quasi total</p>
  ---
  ## Exemples d'utilisation:
  - Je peux insérer une musique youtube dans la partie de 8h à 9h
  - Je peux éxécuter des scripts --> automatisation totale, je peux mettre le mode avion, éteindre l'écran, scrapper tel ou tel site, générer un compte rendu word, poster qqch sur X(Twitter), lancer l'assisstant... 
