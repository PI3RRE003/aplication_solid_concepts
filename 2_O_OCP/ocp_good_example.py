from abc import ABC, abstractmethod

class AproveExam(ABC):

    @abstractmethod
    def aprove_request_exam(self, exam):
        pass
    
    @abstractmethod
    def verify_conditions_exam(self,exam):
        pass




class AproveExamBlood(AproveExam):
    def aprove_request_exam(self, exam):
        if self.verify_conditions_exam(exam):
            print('Blood Exam Aproved')

    def verify_conditions_exam(self, exam):
        return exam.type.lower() == "blood"

class AproveExamXray(AproveExam):
    def aprove_request_exam(self, exam):
        if self.verify_conditions_exam(exam):
            print('X-ray aproved') 

    def verify_conditions_exam(self, exam):
         return exam.type.lower() == "x-ray"

class Exam:
    def __init__(self, type): 
        self.type = type

exam_blood = Exam('Blood') 
exam_x_ray = Exam('X-ray')

aprove_blood = AproveExamBlood()
aprove_x_ray = AproveExamXray()

aprove_blood.aprove_request_exam(exam_blood)
aprove_x_ray.aprove_request_exam(exam_x_ray)