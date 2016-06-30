# Assignment

Here the idea is to use Ansible playbook to configure everything from setting up Ec2 instances ,installing neccessary packages 
and running the flask app.
Below is the description of playbook created for this purpose:
- Solution.yml - This is the playbook which launches the ec2 with all the neccesary parameters like instance type, security group,
region etc. This playbook after launching ec2 ,adds its IP to the inventory file under 'launched' group.It also checks if the ssh 
has come up using one of the modules 'wait_for'. Once the above plays are completed , it then uses role "helloWorldApp" which 
contains all the necessary configuration to run the helloWorld app using Flask.
