resource "aws_security_group" "bastion_sg" {
  name        = "bastion-sg"
  description = "Security group for bastion host"
  vpc_id      = var.vpc

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "bastion" {
  ami           = "ami-0c94855ba95c71c99"
  instance_type = "t3.nano"
  key_name      = var.keyname
  subnet_id     = var.subnetid

  vpc_security_group_ids = [aws_security_group.bastion_sg.id]

  iam_instance_profile = "bastion-role"

}