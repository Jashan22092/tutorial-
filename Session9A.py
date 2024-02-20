from Session9 import Patient , PatientQueue

def main():
    patient1 = Patient("Jashan" , 21 , "Male")
    patient2 = Patient("Simmu", 22, "Male")
    patient3 = Patient("Vansh", 20, "Male")

    queue = PatientQueue()
    print("Initial Queue Is: " , vars(queue))

    queue.enqueue(patient = patient1)
    queue.enqueue(patient=patient2)
    queue.enqueue(patient=patient3)

    print("Queue Now Is: " , vars(queue))

    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    print("Queue Now Is: ", vars(queue))

    queue.iterate()

if __name__ == "__main__":
    main()

