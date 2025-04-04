import torch
import torch.functional as F
from torch.utils.data import Dataset,DataLoader
from torchvision import transforms
from dataset_loader import extract_image_and_bounding_box
from PIL import Image

# first, we need to rehape the image into comman size, then after that we will load the data into the dataloader

class Resizeandnormalization:
    def __init__(self,image:Image.Image,box,image_size=(224,224)):
        self.image_size= image_size
        self.image,self.box=image,box
        
    def __call__(self):
        image_resized=self.image(Image.resize(self.image_size))
        
        #now we will rehape the boundinf box into the same size as the image 
        original_width,original_height=self.image.size
        new_width,new_height=self.image_size
        
        #scale treh bounding box to the new size
        scale_x= new_width/original_width
        scale_y= new_height/original_height
        
        new_box=[]
        
        for i in range(len(self.box)):
            x,y,width, height=self.box[i]
            new_x=int(x*scale_x)
            new_y=int(y*scale_y)
            new_widths=int(width*scale_x)
            new_heights=int(height*scale_y)
            
            new_box.append([new_x,new_y,new_widths, new_heights])
        return image_resized,new_box

    
            
            

class cocodataset_transform(Dataset):
    def __init__(self, image_path, annotation_path, transforms):
        self.image_path = image_path
        self.annotation_path= annotation_path
        self.transform= transforms
        
        
    def __len__(self):
        return len(self.image_id)
    
    def __getitem__(self, index):
        image=self.image[index]
        
        
        
if __name__== "__main__":
    
    annotation_file=r"E:\for practice game\object detection\ObjectDetectNet\dataset\archive (1)\coco2017\annotations\instances_train2017.json"
    images_path=r"E:\for practice game\object detection\ObjectDetectNet\dataset\archive (1)\coco2017\train2017"
        
        
    image_size=(224,224)
    
    image,box,label,image_id=extract_image_and_bounding_box(annotation_file,images_path)
    print(image.shape,box.shape,label.shape,image_id.shape)
    
    resized=Resizeandnormalization(image_size,image,box)
    resized_image,resized_box=resized()
    print(resized_image.shape,resized_box.shape)
    
    
    