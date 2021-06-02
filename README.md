# Template-builder
A command line tool for generating files based on templates.

## Installation on macOS

Open your command line tool and navigate to a directory of your choice where to deposit the template-builder script.
Then run the following command:
```bash
git clone -b master https://github.com/DeveloperZoneIO/template-builder.git && template-builder/install
```
Then run the following command to check if **template-builder** was successully installed:
```bash
tb version
```

If you want to uninstall **template-builder** the run the following command from anywhere in your command line tool:
```bash
uninstall_template_builder
```

## Commands
|Command | Description |
|---------|-----------|
|`tb init`            | Generates a default config JSON in the current working directory
|`tb version`         | Prints the version of the installed **template-builder**
|`tb add <templateFileName>`| Starts the generation of files based on the template matching to the given `<templateFileName>`. The `<templateFileName>` must not contain the **.tbf** extenstion. This template has to be located in the templates directory which is defined in the `template_builder_config.json` (see [Configuration file](#configuration-file))

## Configuration file
Template builder requires you to have a `template_builder_config.json` file in the current working directory. Without it **template builder** will not work properly. Run `tb init` to initialize a default config.

**Config Fields of `template_builder_config.json`:**

- `localTemplates.path` tells the **template builder** where it has to search for template-builder-files. This has to be a local directory on your machine. A template-builder-file contains instructions for how to generate a file and where to put it. 
By default this filed is set to `"templates/"`. This tells the template builder that the template-builder-files are located in the  *templates* directory, which is located in your current work directory.

## The template-builder-file
In order to make the `tb add` command work, add template-builder-files to the *template* folder like mentioned in [Configuration file](#configuration-file) section above.
A template-builder-file uses **.tbf** as file extension. 
A template-builder-file can have three sections: `@_input`, `@_script` and `@_output`.
The sections will be executet from top to bottom in the order you have defined them.

#### `@_input`
The input section is defined by the `@_input` tag. It allows you to define variables with associated prompts. Each variable-prompt pair must be placed on a separate line below the `@_input` tag. A variable-promt pair follows the following scheme: `<variableName>? <some prompt message>`.
The best place for the `@_input` section will be at the very top of the file.

Example:

```kotlin
@_input
userName? Enter your name
userAge? Enter your age
```

#### `@_output`
The output section is defined by the `@_output` tag. It allows you to define the content of the files that should be generated.
Feel free to define as many `@_output` section as you like.

##### Parameters
The output section accepts parameters. They have to be placed below the `@_output` tag. A parameter follows the following scheme: `- <parameterName>? <value>`.
The following example shows what parameters can be defined:

```kotlin
@_output
- path? outputFolder/user_data.txt //this is the relative path from the working directory. This parameter is REQUIRED
- writeFile? false //defaults to true and is OPTIONAL
- replaceExistingFile? false //defaults to true and is OPTIONAL
```

If you want to use variables from the input or script section as parameter values then just wrap them with double curly brackets.

```kotlin
@_output
- path? outputFolder/{{userName}}.txt
- writeFile? {{isWriteFileEnabled}} // has to be a string variable containing "true" or "false"
- replaceExistingFile? {{shouldReplaceExistingFile}} // has to be a string variable containing "true" or "false"
```

##### File content
Below the parameters you can put the file content. If you want to use variables form the input section then just wrap them with double curly brackets. 

```kotlin
@_output
- path? outputFolder/user_data.txt

Hi,
my name is {{userName}} and I'm {{userAge}} years old.
```

#### `@_script`
The script section is defined by the `@_script` tag. It allows you to define and run a custom python script.
It has acces to the variables defined in the `@_input` section, but only if the `@_input` section is
placed above. This is because template-builder executes the sections from top to bottom.
Below the `@_script` tag you can put a custom python script. All global variables defined in the custom script, will be available in the `@_output` section. This means that you can make use of them by putting the varibale names into double curly backtes, like you would do with variables from the `@_input` section.

Feel free to define as many `@_output` section as you like.

Example:
```kotlin
@_input
userName? Enter your name
userAge? Enter your age

@_script
camelCaseName = userName.title() // userName contains the user input because it is defined in the input section above
date = datetime.today().strftime('%Y-%m-%d') // introduces a new variable containing the current date

@_output
- path? outputFolder/user_data.txt
- replaceExistingFile? false
Hi,
my name is {{userName}} and I'm {{userAge}} years old.
Date: {{date}} // this is the date defined in the script section
```