import boto3
import io
from PIL import Image, ImageDraw, ExifTags, ImageColor
if __name__ == "__main__":
    image = Image.open('target_1.jpeg')
    width = image.size[0]
    height = image.size[1]
    bucket='aws-test-rekognition'
    draw = ImageDraw.Draw(image) 
    fileName='target_1.jpeg'
    threshold = 85
    maxFaces=1


    client=boto3.client('rekognition')

  
    response=client.compare_faces(
        
    TargetImage={
        "S3Object": {
            "Bucket": bucket,
            "Name": "target_1.jpeg"
        }
    },
    SourceImage={
        "S3Object": {
            "Bucket": bucket,
            "Name": "source.jpeg"
        }
    },
    SimilarityThreshold=2,
    

    )

                                
    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        similarity = str(faceMatch['Similarity'])
        left = position['Left'] * width
        top = position['Top'] * height
        width_1 = position['Width'] * width
        height_1 = position['Height'] * height
        print('Left: ' + '{0:.0f}'.format(left))
        print('Top: ' + '{0:.0f}'.format(top))
        print('Face Width: ' + "{0:.0f}".format(width_1))
        print('Face Height: ' + "{0:.0f}".format(height_1))

        points = (
            (left,top),
            (left + width_1, top),
            (left + width_1, top + height_1),
            (left , top + height_1),
            (left, top)

        )
        draw.line(points, fill='#00d400', width=5)

    image.show()
        

    


    