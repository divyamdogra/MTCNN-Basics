# MTCNN-Basics

<h3>What is MTCNN?</h3>

MTCNN (Multi-task Cascaded Neural Network) detects faces and facial landmarks on images/videos. This method was proposed by Kaipeng Zhang et al. in their paper ‘Joint Face Detection and Alignment using Multi-task Cascaded Convolutional Networks’, IEEE Signal Processing Letters, Volume: 23 Issue: 10.
The whole concept of MTCNN can be explained in three stages out of which, in the third stage, facial detection and facial landmarks are performed simultaneously. These stages consists of various CNN’s with varying complexities.


<h3>A simpler explanation of the three stages of MTCNN can be as follows : </h3>

In the first stage the MTCNN creates multiple frames which scans through the entire image starting from the top left corner and eventually progressing towards the bottom right corner. The information retrieval process is called P-Net(Proposal Net) which is a shallow, fully connected CNN.

In the second stage all the information from P-Net is used as an input for the next layer of CNN called as R-Net(Refinement Network), a fully connected, complex CNN which rejects a majority of the frames which do not contain faces.

In the third and final stage, a more powerful and complex CNN, known as O-Net(Output Network), which as the name suggests, outputs the facial landmark position detecting a face from the given image/video.
