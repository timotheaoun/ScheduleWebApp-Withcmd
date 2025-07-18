
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
