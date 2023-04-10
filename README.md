### DSCI6007 Sparkify Lab 5

In this lab we scale out using multiple nodes (instances) using Hadoop. A key difference with IPython parallel is that Hadoop is not interactive, it works with batch processes. So in Hadoop, we wrap the processes in a map and a reduce step.
#### **Hadoop**
#### Step 1: Create a Hadoop cluster. 

The Hadoop cluster is created in AWS EMR with the following configuration:

- Launch mode: Cluster
- Applications: Core Hadoop
- Instance type: m4.xlarge
- Number of instances: 3 Choose your EC2 key pair and click "Create cluster".

When the status is *waiting* the cluster is ready to use. Edit inbound rules in the Security Group to enable SSH.

#### Step 2: Create Mapper and Reducer Scripts

- Follow the *Enable an SSH Connection* instructions under the *Application User Interfaces* tab to SSH into the master node of the EMR cluster. 
```
mkdir hadoop_lab
cd hadoop_lab
```
- Create a virtual environment
```
python -m venv venv
source venv/bin/activate
```
- Create and edit the mapper.py and reducer.py scripts
```
vim mapper.py
vim reducer.py
```
- Allow execution permissions
```
chmod a+x mapper.py
chmod a+x reducer.py
```
- Create the *test.json* file using data from one of the log files [previously](https://github.com/rara-by/Sparkify3-4_S3_Parallel_Computing_EC2) uploaded to an S3 bucket.
```
vim test.json
```
- Test the codes
```
cat test.json | ./mapper.py | sort | ./reducer.py 
```
Output (count most frequently played artists)

<img src="https://user-images.githubusercontent.com/63100531/230808731-92c71e90-d33d-4b7d-91a8-88243266c808.png" width="150">

#### Step 3: Running a streaming step
- upload the code files to a different S3 bucket
```
aws configure
aws s3 cp mapper.py s3://emr-mapper-reducer/
aws s3 cp reducer.py s3://emr-mapper-reducer/
```
- Test a streaming jon under the *Steps* tab
<img src="https://user-images.githubusercontent.com/63100531/230809528-36f0fa72-43c1-4766-9238-c0141b52fa89.png" width="450">
The output folder cannot be an existing folder.
The output is in parts:
<img src="https://user-images.githubusercontent.com/63100531/230810401-62cde770-1453-4166-bb7d-723218723047.png" width="480">

