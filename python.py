from collections import defaultdict, Counter
# Lecture du fichier et stockage des données
logs = []
with open("network_log.txt","r",encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.strip()
        if ligne:
            date, heure, ip_source, port, protocole, statut = ligne.split(";")
            entree = {
                "date": date,
                "heure": heure,
                "ip_source":ip_source,
                "port":int(port),
                "protocole":protocole,
                "statut": statut
            }
        logs.append(entree)

# Nombre total de connexions
i = 0
for log in logs:
    i = i +1
print("Nombre total de connexions :",i)


# Nombre total de succès
i = 0
for log in logs:
    if log["statut"]=="SUCCES":
        i = i + 1
print("Nombre total de succès :",i)

# Nombre total d’échecs
i = 0
for log in logs:
    if log["statut"]=="ECHEC":
        i = i + 1
print("Nombre total d’échecs:",i)

# Port le plus utilisé
port_liste = [p["port"] for p in logs]
port_frequent = max(set(port_liste),key=port_liste.count)
print("Port le plus utilisé : Le port ",port_frequent)

# Adresse IP la plus active.
ip_liste = [ip["ip_source"] for ip in logs]
ip_frequent = max(set(ip_liste),key=ip_liste.count)
print("Adresse IP la plus active :", ip_frequent)

# Suspecte
ip_port_echecs = defaultdict(lambda: defaultdict(int))
for l in logs: 
    if l["statut"] == "ECHEC": 
        ip_port_echecs[l["ip_source"]][l["port"]] += 1
ip_suspectes = [] 
for ip, ports in ip_port_echecs.items():
    for port, nb in ports.items(): 
        if nb > 5: 
            ip_suspectes.append((ip, port, nb))

if ip_suspectes:
    for ip, port, nb in ip_suspectes:
        print(f"- {ip} sur le port {port} ({nb} échecs)") 
else: 
    print("- Aucune IP suspecte détectée")

# Top 3 des ports les plus utilisés 
ports = Counter([l["port"] for l in logs]) 
top_ports = ports.most_common(3)
print("Top 3 des ports les plus utilisés :") 
for port, nb in top_ports:
    print(f"- Port {port} : {nb} utilisations")


#rapport_analyse.txt
with open("rapport_analyse.txt", "w", encoding="utf-8") as f:
    f.write("=== Rapport d'analyse réseau ===\n\n")
    f.write("Résumé des statistiques :\n")

