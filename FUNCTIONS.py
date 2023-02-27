#AREA OF A CIRCLE
def area_of_circle(pie,radius):
    area=pie*radius*radius
    return area
print(area_of_circle(3.142,7))


# VOLUME OF A CYLINDER
def volume_of_cylinder(pie,radius,height):
    volume=pie*radius*radius*height
    return volume
print(volume_of_cylinder(3.142,7,12))


#AREA OF A RECTABLE
def area_of_rectangle(length,width):
    area=length*width
    return area
print(area_of_rectangle(20,40))



#VOLUME OF A SPHERE
def volume_of_sphere(pie,radius):
    volume=4/3*pie*radius*radius*radius
    return volume
print(volume_of_sphere(3.142,4))

                                                                                                                                                                                                                                                                              
#VOLUME OF A SPHERE
def area_of_sphere(radius):
    area=3.142*radius*radius
    return area
     
      
print(area_of_sphere(radius=int(input(" Enter the radius: "))))



#CALCULATING COMPOUND INTEREST


principal=int(input("Enter the principal:"))
rate=float(input("Enter the rate:"))
time=int(input("Enter the time:"))

def compound_interest(principal,rate,time):
    amount=principal*(1+rate)**time
    return amount
print(compound_interest(principal,rate,time))


    

    