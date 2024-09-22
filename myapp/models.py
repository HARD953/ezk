from django.db import models
from django.db.models import Sum, F, Func


class Numero(models.Model):
    idNumero = models.AutoField(primary_key=True)
    Numero = models.CharField(max_length=45)
    Quantite = models.IntegerField(default=0)

    def __str__(self):
        return self.Numero

    class Meta:
        db_table = 'Numero'
        verbose_name = 'Numero'
        verbose_name_plural = 'Numeros'


class Marque(models.Model):
    idMArque = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=45)
    Quantite = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.Nom}"

    class Meta:
        db_table = 'Marque'
        verbose_name = 'Marque'
        verbose_name_plural = 'Marques'


class Fournisseur(models.Model):
    idFournisseur = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=45)
    Contact = models.CharField(max_length=45)

    def __str__(self):
        return self.Nom

    class Meta:
        db_table = 'Fournisseur'
        verbose_name = 'Fournisseur'
        verbose_name_plural = 'Fournisseurs'


class Pneu(models.Model):
    idPneu = models.AutoField(primary_key=True)
    Numero = models.ForeignKey(Numero, on_delete=models.CASCADE, default="")
    Details = models.CharField(max_length=45)
    Prix = models.DecimalField(max_digits=10, decimal_places=2)
    Stockage = models.CharField(max_length=45)
    Quantite = models.IntegerField()
    Date = models.DateTimeField()
    Fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    Marque = models.ForeignKey(Marque, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Marque} {self.Numero} {self.Details}"

    class Meta:
        db_table = 'Pneu'
        verbose_name = 'Pneu'
        verbose_name_plural = 'Pneus'


class Client(models.Model):
    idClient = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=45)
    Contact = models.CharField(max_length=45)
    Statut = models.BooleanField(default=True)
    etat_compte = models.IntegerField(default=1)

    def montant_paye_history(self):
        return Historique.objects.filter(Client=self, Designation="Paiement de dette").aggregate(Sum('Montant_Paye'))['Montant_Paye__sum'] or 0
    def montant_restant(self):
        return Historique.objects.filter(Client=self).exclude(Designation="Paiement de dette").aggregate(Sum('Montant_Restant'))['Montant_Restant__sum'] or 0

    def montant_total_restant(self):
        
        latest_record = Historique.objects.filter(Client=self).order_by('-idHistorique').first()
        if latest_record :
            return latest_record.Montant_Restant
        else:
            return 0
        
    def montant_paye(self):
        return Historique.objects.filter(Client=self).exclude(Designation="Remboursement").aggregate(Sum('Montant_Paye'))['Montant_Paye__sum'] or 0

    def montant_total(self):
        return (
            Historique.objects
            .filter(Client=self)
            .annotate(absolute_total=Func(F('Montant_Total'), function='ABS'))
            .aggregate(Sum('absolute_total'))['absolute_total__sum'] or 0
        )

    def __str__(self):
        return self.Nom

    class Meta:
        db_table = 'Client'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Historique(models.Model):
    idHistorique = models.AutoField(primary_key=True)
    Date_Achat = models.DateTimeField()
    Designation = models.CharField(max_length=45)
    Montant_Total = models.DecimalField(max_digits=10, decimal_places=2)
    Montant_Paye = models.DecimalField(max_digits=10, decimal_places=2)
    Montant_Restant = models.DecimalField(max_digits=10, decimal_places=2)
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.Designation

    class Meta:
        db_table = 'Historique'
        verbose_name = 'Historique'
        verbose_name_plural = 'Historiques'


class PneuHistorique(models.Model):
    idPneuHistorique = models.AutoField(primary_key=True)
    Pneu_Numero = models.ForeignKey(Pneu, on_delete=models.CASCADE)
    Historique_idHistorique = models.ForeignKey(Historique, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Pneu_Numero} - {self.Historique_idHistorique}"

    class Meta:
        db_table = 'PneuHistorique'
        verbose_name = 'PneuHistorique'
        verbose_name_plural = 'PneuHistorique'


class Administrateur(models.Model):
    idAdministrateur = models.AutoField(primary_key=True)
    Password = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.Password}"

    class Meta:
        db_table = 'Administrateur'
        verbose_name = 'Administrateur'
        verbose_name_plural = 'Administrateurs'


class Nature(models.Model):
    idNature = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=45, default="")

    def __str__(self):
        return f"{self.Name}"

    class Meta:
        db_table = 'Nature'
        verbose_name = 'Nature'
        verbose_name_plural = 'Natures'


class Transaction(models.Model):
    idTransaction = models.AutoField(primary_key=True)
    Numero = models.ForeignKey(Numero, on_delete=models.CASCADE, default="")
    Details = models.CharField(max_length=45)
    Prix = models.DecimalField(max_digits=10, decimal_places=2)
    Stockage = models.CharField(max_length=45)
    Quantite = models.IntegerField()
    Date = models.DateTimeField()
    Fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    Marque = models.ForeignKey(Marque, on_delete=models.CASCADE)
    Nature = models.ForeignKey(Nature, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f"{self.Marque} {self.Numero} {self.Details}"

    class Meta:
        db_table = 'Transaction'
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'


class Batterie(models.Model):
    idBatterie = models.AutoField(primary_key=True)
    Numero = models.ForeignKey(Numero, on_delete=models.CASCADE, default="")
    Details = models.CharField(max_length=45)
    Prix = models.DecimalField(max_digits=10, decimal_places=2)
    Stockage = models.CharField(max_length=45)
    Quantite = models.IntegerField()
    Date = models.DateTimeField()
    Fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    Marque = models.ForeignKey(Marque, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Marque} {self.Numero} {self.Details}"

    class Meta:
        db_table = 'Batterie'
        verbose_name = 'Batterie'
        verbose_name_plural = 'Batteries'


class Accessoire(models.Model):
    idAccessoire = models.AutoField(primary_key=True)
    Numero = models.ForeignKey(Numero, on_delete=models.CASCADE, default="")
    Details = models.CharField(max_length=45)
    Prix = models.DecimalField(max_digits=10, decimal_places=2)
    Stockage = models.CharField(max_length=45)
    Quantite = models.IntegerField()
    Date = models.DateTimeField()
    Fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    Marque = models.ForeignKey(Marque, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Marque} {self.Numero} {self.Details}"

    class Meta:
        db_table = 'Accessoire'
        verbose_name = 'Accessoire'
        verbose_name_plural = 'Accessoires'


class BatterieHistorique(models.Model):
    idBatterieHistorique = models.AutoField(primary_key=True)
    Batterie_Numero = models.ForeignKey(Batterie, on_delete=models.CASCADE)
    Historique_idHistorique = models.ForeignKey(Historique, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Batterie_Numero} - {self.Historique_idHistorique}"

    class Meta:
        db_table = 'BatterieHistorique'
        verbose_name = 'BatterieHistorique'
        verbose_name_plural = 'BatterieHistorique'


class AccessoireHistorique(models.Model):
    idAccessoireHistorique = models.AutoField(primary_key=True)
    Accesoire_Numero = models.ForeignKey(Accessoire, on_delete=models.CASCADE)
    Historique_idHistorique = models.ForeignKey(Historique, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Accesoire_Numero} - {self.Historique_idHistorique}"

    class Meta:
        db_table = 'AccessoireHistorique'
        verbose_name = 'AccessoireHistorique'
        verbose_name_plural = 'AccessoireHistorique'