# TweetBotUtils
 This repository hosts a few scripts related to the creation and formatting of datasets for bot detection in Twitter datasets.
 
 ## user_dataset_from_davint.py ##
 
 This script creates a user dataset from a collection of tweets in JSON format. `davint` refers to the standard used by [TweetUtils](https://github.com/DAVINTLAB/TweetUtils), however, it should work as long as your JSON file hosts an `id` property that refers to the ID of every tweet. Selenium, Chromedriver, Tweepy, and Twitter API keys are required to run this script.
 
  ## user_dataset_from_uid.py ##
  
  Same usecase as above, but it assumes your tweet dataset contains the `user_id` for every tweet. Runs considerably faster and is much more lightweight considering it's not running on a headless browser to obtain the updated `screen_name`.
  
  
 ## yangetal_from_userset.py ##
 
 Creates a user dataset with the feature set used in [Yang, K.-C., Varol, O., Hui, P.-M., & Menczer, F. (2020). Scalable and Generalizable Social Bot Detection through Data Selection. Proceedings of the AAAI Conference on Artificial Intelligence, 34(01), 1096-1103.](https://ojs.aaai.org/index.php/AAAI/article/view/5460) This script works from using an existing dataset of users created by the previous scripts. Please use the following citation if you end using this in your work:
 
 ```
 @article{Yang_Varol_Hui_Menczer_2020, 
 title={Scalable and Generalizable Social Bot Detection through Data Selection}, 
 volume={34}, 
 url={https://ojs.aaai.org/index.php/AAAI/article/view/5460}, 
 doi={10.1609/aaai.v34i01.5460}, 
 number={01}, 
 journal={Proceedings of the AAAI Conference on Artificial Intelligence},
 author={Yang, Kai-Cheng and Varol, Onur and Hui, Pik-Mai and Menczer, Filippo},
 year={2020}, month={Apr.},
 pages={1096-1103}}
 ```
 
 ## abreuetal_from_userset.py ##
 
 Creates a user dataset with the feature set used in [J. V. Fonseca Abreu, C. Ghedini Ralha and J. J. Costa Gondim, "Twitter Bot Detection with Reduced Feature Set," 2020 IEEE International Conference on Intelligence and Security Informatics (ISI), 2020, pp. 1-6.](https://ieeexplore.ieee.org/abstract/document/9280525) This script works from using an existing dataset of users created by the previous scripts. Please use the following citation if you end using this in your work:
 
 ```
 @inproceedings{9280525,
  author={Fonseca Abreu, Jefferson Viana and Ghedini Ralha, Célia and Costa Gondim, João José},
  booktitle={2020 IEEE International Conference on Intelligence and Security Informatics (ISI)}, 
  title={Twitter Bot Detection with Reduced Feature Set}, 
  year={2020},
  pages={1-6},
  doi={10.1109/ISI49825.2020.9280525}}
 ```
