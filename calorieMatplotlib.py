#implementning matplotlib question
import matplotlib.pyplot as plt
foods=["meat","banana","avacados","sweet potatoes","spinach","watermelon","coconut water","beans","legumes","tomato"]
calories=[250,130,140,120,20,20,10,50,40,19]
potassium=[40,55,20,30,40,32,10,26,25,20]
fat=[8,5,3,6,1,1.5,0,2,1.5,2.5]

#subplot
plt.figure(figsize=(12,6))
#for calories
plt.subplot(1,3,1)
plt.barh(foods,calories,color="skyblue")
plt.xlabel("Calories")
plt.title("Calories in Foods")
#for potassium
plt.subplot(1,3,2)
plt.barh(foods,potassium,color="lightgreen")
plt.xlabel("Potassium")
plt.title("Potassium in Foods")
#for fat
plt.subplot(1,3,3)
plt.barh(foods,fat,color="salmon")
plt.xlabel("Fat")
plt.title("Fat in Foods")


plt.tight_layout
plt.show()