import pandas as pd

mydata={
    'cars': ['Toyota', 'Honda', 'Ford', 'BMW', 'Audi', 'Chevrolet', 'Nissan', 'Hyundai', 'Kia', 'Mazda', 'Subaru', 'Volkswagen', 'Mercedes', 'Lexus', 'Jeep', 'Dodge', 'Ram', 'GMC', 'Cadillac', 'Chrysler', 'Buick', 'Acura', 'Infiniti', 'Lincoln', 'Volvo', 'Mini', 'Fiat', 'Alfa Romeo', 'Mitsubishi', 'Suzuki', 'Saab', 'Pontiac', 'Hummer', 'Scion', 'Smart', 'Genesis', 'Rivian', 'Lucid', 'Polestar', 'Tata', 'Mahindra', 'Proton', 'Perodua', 'Great Wall', 'Chery', 'Geely', 'BYD', 'NIO', 'XPeng', 'Li Auto', 'Canoo', 'Fisker'],
    'speed': [120, 130, 125, 150, 160, 140, 135, 128, 132, 138, 145, 155, 165, 170, 142, 148, 152, 158, 162, 168, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300],
}
df = pd.DataFrame(mydata)
print(df)