<div align="center">

# To Do List <br>

### A To Do List for your terminal.
</div>

## Installation
Installing the program is very easy. Download your preffered native OS To Do List:
[ToDoList-Windows](https://github.com/Itsmemonzu/ToDoList/releases/download/0.1/main.exe),

There you have it! The app is now installed. 
Please note: If your OS is not listed above, you will have to build the program your self by downloading the source code.
<br>

## Building
This program is dependant on [Rich](https://github.com/Textualize/rich?tab=readme-ov-file). To build the program, you need to use Pyinstaller or a compiler of your choice:
```
pip install pyinstaller
```

To compile using Pyinstaller, run this:

```bash
$ pyinstaller --onefile main.py
```

Finally, Your build will be located in: `ToDoList\dist\`

<br>

## Running

Once the build is complete, you can simply open the file or run it through your terminal in the build directory and type:

```bash
$ .\main.exe (Change the main.exe to your build file)
```


<br>

## Contribution
Contributing to Tale is simple. You have to fork the repository and clone it. Make your changes. After you are done, just push the changes to your fork and make a pull request. 

I hope that you will be making some amazing changes!

<br>

## License

Licensed under the [MIT License](./LICENSE).
