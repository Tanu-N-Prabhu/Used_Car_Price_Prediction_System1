from django import forms
"""
This nameOfTheCarForm class is used for storing the name of the car.
    @Author: Tanu Nanda Prabhu
    @Parameters:
        forms.Forms: This is a default form provided by Django
    File Reference: home.html
""" 
COLOR_CHOICES = (
    (1, 'Limousine'),
    (2, 'Station Wagon'),
    (3,'Bus'),
    (4,'Convertible'),
    (5, 'Coupe'),
    (6, 'SUV'),
    (7, 'Small Car'),
    (8, 'Others')
)

Gearbox = (
    (1, 'Manual'),
    (2, 'Automatic')
)

Year = (
(1995, 1995),
(1996, 1996),
(1997, 1997),
(1998, 1998),
(1999, 1999),
(2000, 2000),
(2001, 2001),
(2002, 2002),
(2003, 2003),
(2004, 2004),
(2005, 2005),
(2006, 2006),
(2007, 2007),
(2008, 2008),
(2009, 2009),
(2010, 2010),
(2011, 2011),
(2012, 2012),
(2013, 2013),
(2014, 2014),
(2015, 2015),
(2016, 2016),
(2017, 2017),
(2018, 2018),
(2019, 2019),
)

Month = (
    (1, 1),(2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)
)


Brand = (
    (0, 'alfa_romeo'),        
    (1, 'audi'),              
    (2, 'bmw'),               
    (3, 'chevrolet'),           
    (4, 'chrysler'),           
    (5, 'citroen'),            
    (6, 'dacia'),              
    (7, 'daewoo'),              
    (8, 'daihatsu'),             
    (9, 'fiat'),               
    (10,'ford'),              
    (11, 'honda'),              
    (12, 'hyundai'),            
    (13, 'jaguar'),              
    (14, 'jeep'),                
    (15, 'kia'),                
    (16, 'lada'),                  
    (17, 'lancia'),              
    (18, 'land_rover'),          
    (19, 'mazda'),              
    (20, 'mercedes_benz'),     
    (21, 'mini'),               
    (22, 'mitsubishi'),         
    (23, 'nissan'),             
    (24, 'opel'),              
    (25, 'peugeot'),            
    (26, 'porsche'),            
    (27, 'renault'),            
    (28, 'rover'),               
    (29, 'saab'),                
    (30, 'seat'),               
    (31, 'skoda'),              
    (32, 'smart'),                
    (33, 'sonstige_autos'),     
    (34, 'subaru'),              
    (35, 'suzuki'),              
    (36, 'toyota'),             
    (37, 'volkswagen'),        
    (38, 'volvo'),              
)


Model = (
    (11,'3 er'),(114, 'Grand'),(8,'2 Series'), (58,'C Max'),(10,'3 Series'), (98, 'Fabia')
)


Fuel = (
    (1, 'Petrol'), (2, 'CNG'), (3, 'Diesel'), (4, 'Electronic'), (5, 'Hybrid'), (6, 'LPG')
)

class nameOfTheCarForm(forms.Form):
    
    carYearOfRegistration = forms.IntegerField(label=' ', widget=forms.Select(choices=Year))
    def clean_carYearOfRegistration(self):
        carYearOfRegistration = self.cleaned_data['carYearOfRegistration']
        if carYearOfRegistration == 1000:
            raise forms.ValidationError("Year of Registration is not valid")
        return carYearOfRegistration

    carPower = forms.IntegerField(label = '', widget=forms.TextInput(attrs={'placeholder':'  Power of the car (PS)'}))
    carModel = forms.IntegerField(label=' ', widget=forms.Select(choices=Model))
    carKilometer = forms.IntegerField(label = '', widget=forms.TextInput(attrs={'placeholder':'  Total Kilometers'}))
    carMonth = forms.IntegerField(label=' ', widget=forms.Select(choices=Month))

    carFuelType = forms.IntegerField(label=' ', widget=forms.Select(choices=Fuel))
    carBrand = forms.IntegerField(label=' ', widget=forms.Select(choices=Brand))
    carPostalCode = forms.IntegerField(label = '', widget=forms.TextInput(attrs={'placeholder':'  Postal Code'}))
    carVehicleType = forms.CharField(label=' ', widget=forms.Select(choices=COLOR_CHOICES))
    carGearBox = forms.CharField(label='', widget=forms.Select(choices=Gearbox))
    carName = forms.CharField(label = '', widget=forms.TextInput(attrs={'placeholder':'  Enter the name of the car'}))



   

            

