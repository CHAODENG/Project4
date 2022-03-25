# Project4
## A queue system to manage speech to text
### Test for Multiprocess

The test program shows that my computer runs eight API simultaneously which means it could run at most 8 different API at the same time.

And I create 20 task to be run in the program. We can see once task 0 has been done, the next task could run now which has the same process ID with the task 0.

<img width="377" alt="image" src="https://user-images.githubusercontent.com/90479627/160195506-910e926f-8bbc-4a6e-a3c3-456dba8f9a48.png"><img width="527" alt="image" src="https://user-images.githubusercontent.com/90479627/160196319-5d8605ed-e37e-4bc2-8b78-f2d8f58c894a.png">



### Speech to Text Module

Based on the multiprocessing, we could design a queue system to run Speech to Text Module. And this convertor API is using google speech recognition like this.   
<img width="524" alt="image" src="https://user-images.githubusercontent.com/90479627/160194991-44abf007-3db7-4c57-9123-bd8a8b4ae36f.png">

Then I use all cores in my computer to do the test. And the below is what the result looks like:

<img width="800" alt="image" src="https://user-images.githubusercontent.com/90479627/160195755-f8695c31-6daa-4d8e-8449-49020d2406f9.png"><img width="200" alt="image" src="https://user-images.githubusercontent.com/90479627/160196974-dfddb445-f2a1-44d1-94a9-d3c1ea26418f.png">

We find that speech to text module has been called 8 times at first. And the rest task could be run only after one of the processes is done. 

## Reference
* Speech to Text Module: https://towardsdatascience.com/easy-speech-to-text-with-python-3df0d973b426
* Audio Sample Download: https://www.voiptroubleshooter.com/open_speech/american.html







