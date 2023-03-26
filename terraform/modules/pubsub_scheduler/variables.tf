variable "scheduler_name" {
    type = string
    description = "Name of the scheduler job"
}

variable "project_id" {
    type = string
    description = "The project ID to deploy to"
}

variable "region" {
    type = string
    description = "The region to deploy to"
}

variable "description" {
    type = string
    description = "The description of the scheduler job"
    default = ""
    }

variable "schedule" {
    type = string
    description = "The schedule of the scheduler job"
}

variable "time_zone" {
    type = string
    description = "The time zone of the scheduler job"
}   

variable "topic_id" {
    type = string
    description = "The topic ID of the scheduler job"
}   

variable "attributes" {
    type = map(string)
    description = "The attributes of the scheduler job"
    default = null
}   

variable "data" {
    type = string
    description = "The data of the scheduler job"
    default = null
}   

