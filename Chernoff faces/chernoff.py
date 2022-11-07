from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler()
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Arc, Polygon, Wedge
import matplotlib.path as mpath
import pandas as pd
import numpy as np

Path = mpath.Path

class ChernoffFaces:  
  DATA = {
    "HAIR_COLOR": None,
    "HAIR_LEFT": None,
    "HAIR_RIGHT": None,
    "EYEBROW_CURVATURE": None,
    "EYE_HEIGHT": None,
    "PUPIL_SIZE": None,        
    "NOSE_WIDTH": None,
    "MOUTH_HEIGHT": None,
    "MOUTH_WIDTH": None,
    "SKIN_COLOR": None,    
  }

  def __init__(
      self, 
      df, 
      labels=None, 
      filename='faces'
  ):
    if not labels:
      self.labels = df.iloc[:,0].values
      df = df[df.columns.drop(df.columns[0])]
    
    self.data = pd.DataFrame(
      min_max_scaler.fit_transform(df.values), 
      columns=df.columns
    )

    for index, key in enumerate(self.DATA.keys()):
      self.DATA[key] = self.data[self.data.columns[index % len(self.data.columns)]].values.tolist()

    self.filename = filename

  def render_face(self, ax, title='', index=None):
    height, width = ax.bbox.height, ax.bbox.width
  

    self.draw_hair(ax, index, width, height)
    self.draw_face(ax, index, width, height)
    self.draw_brows(ax, index)
    self.draw_eyes(ax, index)
    self.draw_pupils(ax, index)
    self.draw_nose(ax, index)   
    self.draw_mouth(ax, index)


    ax.title.set_text(f"{title}")

    ax.axis('off')
    ax.autoscale()

  def draw_hair(self, ax, index, width, height):
    hair_width = width
    hair_height = height

    colour = plt.cm.coolwarm(self.DATA["HAIR_COLOR"][index])

    trapeze = Polygon(
      xy=[
        [0, hair_height * 0.5 * (1 - self.DATA["HAIR_LEFT"][index])],
        [0, hair_height * 0.5],
        [hair_width, hair_height * 0.5],
        [hair_width, hair_height * 0.5 * (1 - self.DATA["HAIR_RIGHT"][index])],
      ], 
      fc=colour
    )
    ax.add_patch(trapeze)

    top = Wedge(
      center=[hair_width / 2, hair_height * 0.5 - 1], 
      r=hair_width / 2,
      theta1=0, 
      theta2=180,
      edgecolor='none', 
      fc=colour,
    )
    ax.add_patch(top)

  def draw_face(self, ax, index, width, height):
    face_width = width * 2/3
    face_height = height * 1/2
    self.UNIT_WIDTH = face_width / 7
    self.UNIT_HEIGHT = face_height / 7
    self.FACE_CENTER = [width / 2, height / 2]

    colour = plt.cm.coolwarm(self.DATA["SKIN_COLOR"][index])

    ellipse = Ellipse(
      xy=self.FACE_CENTER, 
      width=face_width, 
      height=face_height, 
      edgecolor='black', 
      fc=colour, 
      lw=2
    )
    ax.add_patch(ellipse)
  
  def draw_brows(self, ax, index):
    brow_width = self.UNIT_WIDTH * 1.5
    brow_height =  self.UNIT_HEIGHT * self.DATA["EYEBROW_CURVATURE"][index]
    if brow_height == 0:
      brow_height = 0.001

    brow_l_center = [sum(i) for i in zip(*[ 
      self.FACE_CENTER, 
      [brow_width,  self.UNIT_HEIGHT * 1.1] 
    ])]

    brow_r_center = [sum(i) for i in zip(*[ 
      self.FACE_CENTER, 
      [-brow_width,  self.UNIT_HEIGHT * 1.1] 
    ])]

    brow_l = Arc(
      xy=brow_l_center, 
      width=brow_width, 
      height=brow_height, 
      theta1=0, 
      theta2=180,
      edgecolor='black', 
      fc='None', 
      lw=2
    )
    ax.add_patch(brow_l)

    brow_r = Arc(
      xy=brow_r_center, 
      width=brow_width, 
      height=brow_height, 
      theta1=0, 
      theta2=180,
      edgecolor='black', 
      fc='None', 
      lw=2
    )
    ax.add_patch(brow_r)

  def draw_eyes(self, ax, index):
    eye_width = self.UNIT_WIDTH * 1.5
    eye_height =  self.UNIT_HEIGHT * self.DATA["EYE_HEIGHT"][index] 
    if eye_height == 0:
      eye_height = 0.001

    eye_l_center = [sum(i) for i in zip(*[ 
      self.FACE_CENTER, 
      [-eye_width,  self.UNIT_HEIGHT / 2] 
    ])]

    eye_r_center = [sum(i) for i in zip(*[ 
      self.FACE_CENTER, 
      [eye_width,  self.UNIT_HEIGHT / 2] 
    ])]

    ellipse = Ellipse(
      xy=eye_l_center, 
      width=eye_width, 
      height=eye_height, 
      edgecolor='black', 
      fc='white', 
      lw=1
    )
    ax.add_patch(ellipse)

    ellipse = Ellipse(
      xy=eye_r_center, 
      width=eye_width, 
      height=eye_height, 
      edgecolor='black', 
      fc='white', 
      lw=1
    )
    ax.add_patch(ellipse)   

  def draw_pupils(self, ax, index):
    pupil_width = self.UNIT_WIDTH * self.DATA["PUPIL_SIZE"][index] 
    pupil_height = pupil_width
    eye_width = self.UNIT_WIDTH * 1.5
    if pupil_height == 0:
      pupil_height = 0.001

    pupil_l_center = [sum(i) for i in zip(*[ 
      self.FACE_CENTER, 
      [-eye_width,  self.UNIT_HEIGHT / 2] 
    ])]

    pupil_r_center = [sum(i) for i in zip(*[ 
      self.FACE_CENTER, 
      [eye_width,  self.UNIT_HEIGHT / 2] 
    ])]

    ellipse = Ellipse(
      xy=pupil_l_center, 
      width=pupil_width, 
      height=pupil_height, 
      edgecolor='black', 
      fc='black', 
      lw=1
    )
    ax.add_patch(ellipse)

    ellipse = Ellipse(
      xy=pupil_r_center, 
      width=pupil_width, 
      height=pupil_height, 
      edgecolor='black', 
      fc='black', 
      lw=1
    )
    ax.add_patch(ellipse)   

  def draw_nose(self, ax, index):
    nose_width = self.UNIT_WIDTH * (1 - self.DATA["NOSE_WIDTH"][index])
    nose_height =  self.UNIT_HEIGHT  

    pivot_left = [sum(i) for i in zip(*[ 
      self.FACE_CENTER, 
      [-nose_width / 2,  -nose_height] 
    ])]
    
    pivot_right = [sum(i) for i in zip(*[ 
      self.FACE_CENTER, 
      [nose_width / 2,  -nose_height] 
    ])]

    pivot_top = self.FACE_CENTER

    points = np.array([pivot_left, pivot_right, pivot_top])
    nose = plt.Polygon(
      points, 
      closed=True, 
      lw=1,
      fc="black", 
      edgecolor='black',
    )
    ax.add_patch(nose)

  def draw_mouth(self, ax, index):
    mouth_width = self.UNIT_WIDTH * 3 * self.DATA["MOUTH_WIDTH"][index] 
    mouth_height = self.UNIT_HEIGHT * 1.5 * self.DATA["MOUTH_HEIGHT"][index] 

    mouth_center = [sum(i) for i in zip(*[ 
      self.FACE_CENTER, 
      [0,  -self.UNIT_HEIGHT * 2] 
    ])]

    ellipse = Ellipse(
      xy=mouth_center, 
      width=mouth_width, 
      height=mouth_height, 
      edgecolor='black', 
      fc="black",  
      lw=1
    )
    ax.add_patch(ellipse)

  def render(
      self,
      n_cols=1, 
      n_rows=1,
      figsize=(2, 2),
      empty_cols_ids=None
  ):
    fig, ax = plt.subplots(
      nrows=n_rows, 
      ncols=n_cols, 
      figsize=figsize, 
      sharey=True,
      sharex=True,
      constrained_layout=True,
      frameon=False,
    )

    axes = ax.flatten()

    j = 0
    for i in range(len(axes)):
      ax = axes[i]
      if i in empty_cols_ids:
        ax.remove()
      else:
        self.render_face(ax, title=self.labels[j], index=j)
        j += 1

    plt.savefig(f"{self.filename}.png", bbox_inches="tight")
    plt.close()