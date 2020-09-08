import cv2
# 1 average size calories
calorie_map={
	'apple':95,
	'banana':111,
	'carrot':25,
	'egg':78,
	'mango':201,
	'kiwi':42,
	'tomato':22,
	'orange':62
}

def compute_calorie(food):
	total_calorie = 0.0
	for item in food.keys():
		if item!="coin":
			print('%d %s = %.2f calories' % (food[item],item,food[item]*calorie_map[item]))
			total_calorie += food[item]*calorie_map[item]
	return total_calorie

def show_calorie_on_image(img,food,total_cal):
		font = cv2.FONT_HERSHEY_SIMPLEX 
		fontScale = 1
		color_text = (255, 0, 0) 
		i = 0
		tl = round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1
		tl = max(tl-1,1)
		h = img.shape[0]
		w = img.shape[1]
		mar = h//30
		text_h = (h//10)
		text_w = (w//10)
		for item in food.keys():
			if(item=="coin"):
				continue
			next_text = mar*i
			j = '%d %s : %d calories' % (food[item],item,food[item]*calorie_map[item])
			cv2.putText(img,j,(text_w,text_h+next_text),0,fontScale,[0,0,0],thickness=tl)
			i+=1
		i-=1
		next_text = mar*i
		offset = int(0.5*mar)
		cv2.line(img,(text_w,text_h+next_text+offset),(5*text_w,text_h+next_text+offset),(0,0,0),tl)
		i+=2
		next_text = mar*i
		cv2.putText(img,"Total average calorie : "+str(total_cal),(text_w,text_h+next_text),0,fontScale,[0,0,0],thickness=tl)
