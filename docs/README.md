## Compiling the ER diagram

### Download and setup plantUML

- Download plantUML jar file (http://plantuml.com/) and put in desired location
    
- Append the following to ~/.bashrc and update the path:


```
    plantuml() {
      if [ -f "$1" ]; then
        java -jar /path/to/plantuml.jar $1
      else
        echo "File does not exist"
     fi
    }
```

- Reload bashrc:

```
    source ~/.bashrc
```

### Run on ER.uml

```
    plantuml ER.uml
```