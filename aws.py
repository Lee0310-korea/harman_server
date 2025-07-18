import boto3

def detect_labels_local_file(photo):

    client = boto3.client('rekognition')
   
    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
    
    result = []

    for label in response["Labels"]:
        name = label["Name"]
        confidence = label["Confidence"]

        result.append(f"{name} : {confidence:.2f}%")

    r = "<br/>".join(map(str, result))
    return r

def compare_faces(sourceFile, targetFile):

    client = boto3.client('rekognition')

    imageSource = open(sourceFile, 'rb')
    imageTarget = open(targetFile, 'rb')

    response = client.compare_faces(SimilarityThreshold=80,
                                    SourceImage={'Bytes': imageSource.read()},
                                    TargetImage={'Bytes': imageTarget.read()})

    for faceMatch in response['FaceMatches']:
        similarity = faceMatch['Similarity']
        
    imageSource.close()
    imageTarget.close()
    return f"두 얼굴의 일치율 {similarity:.2f}% 입니다"

def compare_face_main():
    source_file = 'file1'# 비교할 사진
    target_file = 'file2'# 비교할 대상 사진 
    face_matches = compare_faces(source_file, target_file)
    print(f"동일 인물일 확률은 {face_matches:.2f}%입니다")
  
