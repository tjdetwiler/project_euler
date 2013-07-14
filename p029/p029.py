



def main():
    
    X = []
    for a in range(2,101):
        for b in range(2,101):
            z = a**b
            X.append(z)
    
    XX = list(set(X))
    print len(XX)




if __name__ == "__main__":
    main()
