# Behavioral Preparation[^CC150] 
## What questions should you ask the interviewer?
**Genuine Questions**: 
* How much of your day do you spend coding?
* How many meetings do you have every week?
* What is the ratio of testers to developers to product managers?  What is the interac -tion like?  How does project planning happen on the team?

**Insightful Questions**:
* I noticed that you use technology X.  How do you handle problem Y?
* Why did the product choose to use the X protocol over the Y protocol?  I know it has 
bene!ts like A, B, C, but many companies choose not to use it because of issue D .

**Passion Questions**
* I'm very interested in scalability.  Did you come in with a background in this, or what 
opportunities are there to learn about it? 
* I'm not familiar with technology X, but it sounds like a very interesting solution .  
Could you tell me a bit more about how it works?

## How to Prepare for Technical Questions
* Try to solve the problem on your own. 
   Ask yourself if you could improve the time 
   efficiency by reducing the space efficiency, or vice versa.
* Write the code for the algorithm on paper. 
* Type your paper code as-is into a computer.
* Do a mock interview.

## Ask Good Questions Using S.A.R
Structure your responses using S .A.R.: Situation, Action, Response .  That is, you should start 
off outlining  the  situation,  then  explaining  the  actions  you  took,  and  lastly,  describing  the 
result . 

Example: "Tell me about a challenging interaction with a teammate."

**Situations:** On  my  operating  systems  project,  I  was  assigned  to  work  with  three  other 
people .    While  two  were  great,  the  third  team  member  didn't  contribute  much .    He 
stayed quiet during meetings, rarely chipped in during email discussions, and struggled 
to complete his components . 

**Action:**
One  day  after  class,  I  pulled  him  aside  to  speak  about  the  course  and  then 
moved the discussion into talking about the project.  I asked him open-ended questions 
on how he felt it was going, and which components he was excited about tackling.  He 
suggested all the easiest components, and yet offered to do the write-up.  I realized then 
that he wasn't lazy – he was actually just really confused about the project and lacked 
confidence.  I worked with him after that to break down the components into smaller 
pieces, and I made sure to complement him a lot on his work to boost his confidence.

**Result:**
He was still the weakest member of the team, but he got a lot better .  He was 
able  to finish  all  his  work  on  time,  and  he  contributing  more  in  discussions .   We  were 
happy to work with him on a future project .

# Ask Good Quesions in Technical Interview[^offerblade]
面试是一个双向交流的过程，面试官可以问应聘者问题，同样应聘者也可以向面试官提问。
如果应聘者能够针对面试题主动地提出几个高质量的问题，面试就会觉得他有很强的
沟通能力和学习能力。

举个例子，google曾经有一道面试题：找出第1500个丑数。很多人都不知道丑数是什么。
不知道怎么办？面试官就坐在对面，可以问他。面试官会告诉你只含有2、3、5三个因子
的数就是丑数。你听了以后，觉得听明白了，但不太确定，于是可以举几个例子并让
面试官确认你的理解是不是正确：6、8、10、12都是丑数，但14就不是，对吗？
问题问的是第1500个丑数，与顺序有关。可是哪个数字是第一个丑数呢，1是不是第一个？
这个你可能也不能确定，怎么办？还是问面试官，他会告诉你1是或者不是丑数。

最近很流行的一个面试题，面试官最开始问：如何求树中两个结点的最低公共祖先。
此时面试官对题中的特点完全没有给出描述，他希望应聘者在听到问题后会提出几个问题，
比如这棵树是二叉树还是普通的树。

如果面试官说是二叉树，应聘者可以继续问该树是不是排序的二叉树。面试官回答是
排序的。听到这里，应聘者才能确定思路：从树的根节点出发遍历树，如果当前结点
都大于输入的两个结点，则下一步遍历当前结点的左子树；如果当前结点小于输入的
两个结点，则下一步遍历当前结点的右子树。一直遍历到当前结点比一个输入结点大
而比另一个小的时候，此时当前结点就是符合要求的最低公共结点。

在应聘者问树是不是二叉树的时候，如果面试官回答是任意的树，此时应聘者可以接着提问
在树结点中有没有指向父节点的指针。如果面试官给出肯定的回答，也就是树的结点
中有指向父节点的指针，此时从输入的结点出发，沿着指向父节点的指针一直到树的根
结点，可以看作一个链表，因此这个题目的解法就和求两个链表的第一个公共结点的解法
是一样的了。如果面试官给出的是否定的回答，也就是树的结点没有指向父节点的指针，
那么我们可以在遍历的时候用一个栈来保存从根节点到当前结点的路径，最终把它转化为
求两个路径的最后一个公共结点。

当觉得题目的条件、要求不够明确的时候，我们一定要多提问以消除自己的疑惑。

[^CC150]: Cracking the Coding Interview 4th Edition.
[^offerblade]: 剑指offer,名企面试官精讲典型编程题, 何海涛著.
