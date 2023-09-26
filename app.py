from super_gradients.training import models
import torch
import supervision as sv
import gradio as gr 

DEVICE = 'cuda' if torch.cuda.is_available() else "cpu"
MODEL_ARCH = 'yolo_nas_l'
clasess = ["Airplane"]
checkpoint_path= "average_model.pth"


def run(image , CONFIDENCE_TRESHOLD) : 
  best_model = models.get(
      MODEL_ARCH,
      num_classes=len(clasess),
      checkpoint_path= checkpoint_path
  ).to(DEVICE)
  result = list(best_model.predict(image, conf=CONFIDENCE_TRESHOLD))[0]
  detections = sv.Detections(
          xyxy=result.prediction.bboxes_xyxy,
          confidence=result.prediction.confidence,
          class_id=result.prediction.labels.astype(int)
      )
  box_annotator = sv.BoxAnnotator()
  annotated_frame = box_annotator.annotate(
      scene=image.copy(),
      detections=detections,
      labels=clasess
  )
  return annotated_frame
iface = gr.Interface(
    fn=run,
    inputs=[gr.Image(label="Input image", type="numpy") , gr.Slider(0, 1, value=0.5, label="Select your CONFIDENCE_TRESHOLD")],
    outputs=gr.Image(label="The Prediction Output :", type="numpy"),
    title="Aerial Airport YOLO Nas object detection",
    allow_flagging=False , 
    description="I conducted fine-tuning on the YOLO-NAS (YOLO Neural Architecture Search) model, a cutting-edge object detection architecture developed by Deci-AI. My objective was to enhance its ability to detect airplanes in the 'Aerial Airport' dataset",
)
iface.launch(debug=True)
