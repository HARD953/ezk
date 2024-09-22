document.addEventListener("DOMContentLoaded", function () {
    var addRowBtn = document.getElementById("addRowBtn");
    var nombreDeLignesInput = document.getElementById("nombre_de_lignes");
    var form = document.querySelector("form.ajout");
    var table = document.getElementById("tableID");
    var label = document.getElementById("label");

    addRowBtn.addEventListener("click", function () {
        // Récupérer le nombre de lignes à ajouter
        var nombreDeLignes = parseInt(nombreDeLignesInput.value);

        // Cacher l'input et le bouton après le premier clic
        nombreDeLignesInput.style.display = "none";
        addRowBtn.style.display = "none";
        label.style.display = "none";

        // Récupérer la liste des marques via une requête HTTP
        var urls = ["/get_marques", "/get_natures", "/get_numeros"];

        // Récupérer la liste des marques via une requête HTTP
        Promise.all(urls.map(url =>
            fetch(url)
                .then(response => response.json())
        ))
            .then(dataArray => {
                // dataArray contient les résultats de toutes les requêtes
                var marquesData = dataArray[0]; // Résultat de la première requête
                var naturesData = dataArray[1];
                var numerosData = dataArray[2];
                // Boucle pour créer les lignes
                for (let i = 1; i <= nombreDeLignes; i++) {
                    // Créer une nouvelle ligne
                    var nouvelleLigne = table.insertRow();

                    // Créer des cellules avec IDs et names dynamiques
                    var champs = ["nature", "marque", "numero", "details", "prix", "quantite"];
                    for (let champ of champs) {
                        if(champ === "nature"){
                            var cellule = nouvelleLigne.insertCell();
                            var selectHtml = `<select name="${champ}_${i}" id="${champ}_${i}" required style="font-size: 15px;">`;

                            // Ajouter les options de sélection basées sur la liste des marques
                            naturesData.natures.forEach(function (nature) {
                                selectHtml += `<option value="${nature}">${nature}</option>`;
                            });

                            selectHtml += `</select>`;
                            cellule.innerHTML = selectHtml;
                        } else if (champ === "marque") {
                            var cellule = nouvelleLigne.insertCell();
                            var selectHtml = `<select name="${champ}_${i}" id="${champ}_${i}" required style="font-size: 15px;">`;

                            // Ajouter les options de sélection basées sur la liste des marques
                            marquesData.marques.forEach(function (marque) {
                                selectHtml += `<option value="${marque}">${marque}</option>`;
                            });

                            selectHtml += `</select>`;
                            cellule.innerHTML = selectHtml;
                        }else if (champ === "numero") {
                            var cellule = nouvelleLigne.insertCell();
                            var selectHtml = `<select name="${champ}_${i}" id="${champ}_${i}" required style="font-size: 15px;">`;

                            // Ajouter les options de sélection basées sur la liste des marques
                            numerosData.numeros.forEach(function (numero) {
                                selectHtml += `<option value="${numero}">${numero}</option>`;
                            });

                            selectHtml += `</select>`;
                            cellule.innerHTML = selectHtml;
                        }
                        
                        else if(champ === "prix" || champ === "quantite"){
                            var cellule = nouvelleLigne.insertCell();
                            cellule.innerHTML = `<input type="number" oninput="calculer()" name="${champ}_${i}" id="${champ}_${i}" required style="font-size: 15px; max-width: 100px;" />`;
                        }
                        else if(champ === "details"){
                            var cellule = nouvelleLigne.insertCell();
                            cellule.innerHTML = `<input type="text" name="${champ}_${i}" id="${champ}_${i}" style="font-size: 15px; max-width: 100px;" />`;
                        }
                        else {
                            var cellule = nouvelleLigne.insertCell();
                            cellule.innerHTML = `<input type="text" name="${champ}_${i}" id="${champ}_${i}" required style="font-size: 15px; max-width: 100px;" />`;
                        }
                    }

                    // Ajouter une cellule pour le résultat
                    var resultatCellule = nouvelleLigne.insertCell();
                    resultatCellule.id = `resultat_${i}`;
                }

                // Fonction pour calculer le montant total
                function calculer() {
                    var total = 0;
                    for (let i = 1; i <= nombreDeLignes; i++) {
                        // Récupérer les valeurs des champs "prix" et "Quantite"
                        var prix = parseFloat(document.getElementById(`prix_${i}`).value) || 1;
                        var quantite = parseInt(document.getElementById(`quantite_${i}`).value) || 1;

                        // Calculer le montant total
                        var montantTotal = prix * quantite;

                        total = total + montantTotal;

                        // Mettre à jour la cellule "resultat" pour cette ligne
                        document.getElementById(`resultat_${i}`).textContent = montantTotal;
                    }
                    document.getElementById(`resul`).textContent = total;
                    var montant_verse = document.getElementById(`montant_verse`).value || 1;
                    var reste = total - montant_verse;
                    document.getElementById(`reste`).textContent = reste;
                }

                // Associer la fonction calculer() aux événements de changement dans les champs "prix" et "Quantite"
                for (let i = 1; i <= nombreDeLignes; i++) {
                    document.getElementById(`prix_${i}`).addEventListener("input", calculer);
                    document.getElementById(`quantite_${i}`).addEventListener("input", calculer);
                    document.getElementById(`montant_verse`).addEventListener("input", calculer);
                }
            })
            .catch(error => console.error('Erreur lors de la récupération des marques:', error));
    });
});
