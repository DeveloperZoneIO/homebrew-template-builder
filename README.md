# Template-builder
A command line tool for generating files based on templates.

## Installation on macOS

Open your command line tool and navigate to a directory of your choice where to deposit the template-builder script.
Then type in the following command:
```bash
$ git clone -b master https://github.com/DeveloperZoneIO/template-builder.git && template-builder/install
```
Check if `tb` was successully installed by runnig:
```bash
$ tb version
```

You can also uninstall the template builder by running the following command:
```bash
$ uninstall_template_builder
```

## Commands
- `tb init` Generates a default config JSON in the working directory
- `tb version` Prints the version of the installed template builder
- `tb add <templateFileName>` Starts the process of generating a file base on the template with matches the given `templateFileName`

## Basics
Template builder requires you to have a `template_builder_config.json` inside the directory you are currently working in. You can create a default config via `$ tb init`.
The value of `localTemplates.path` inside `template_builder_config.json` tells the **template builder** where it has to search for template-builder-files. This has to be a local directory on your machine. A template-builder-file contains instructions for the template builder so that it knows how and what it has to generate. 
By default `localTemplates.path` is set to `"templates/"`. This tells the template builder that it should use the templates from the directory with the name *templates*, which is located inside your current work directory.

## The template-builder-file
In order to make the `tb add` command work, please add template-builder-files to the *template* folder like mentioned in [Basics](#basics).
A template-builder-file uses **.tbf** as file extension and it allows you to define three sections: `input`, `script` and `output`.

#### Input section
The input section is defined by the `@_input` tag. It allows to define variables with associated prompts. Each variable-prompt pair must be on a separate line below the `@_input` tag. A variable-promt pair follows the following scheme: `<variableName>? <some prompt message>`. 

Input section example:

```kotlin
@_input
userName? Enter your name
userAge? Enter your age
```

#### Output section
The output section is defined by the `@_output` tag. It allows to define the files content which should be generated.

##### Define parameters
The output section accepts parameters. They have to be defined below the `@_output` tag. A parameter definition follows the following scheme: `- <parameterName>? <value>`.
The following example shows what parameters can be defined:

```kotlin
@_output
- path? outputFolder/user_data.txt //this is the relative path from the working directory. This parameter is REQUIRED
- writeFile? false //defaults to true and is OPTIONAL
- replaceExistingFile? false //defaults to true and is OPTIONAL
```

If you want to use variables from the input section in the parameters values then just wrap them with double curly brackets.

```kotlin
@_output
- path? outputFolder/{{userName}}.txt
```

##### Define file content
Below the parameters you can add the files content. If you want to use variables form the input section then just wrap them with double curly brackets. 

Example:
```kotlin
@_output
- path? outputFolder/user_data.txt

Hi,
my name is {{userName}} and I'm {{userAge}} years old.
```

#### Full example of a .tbf file
```kotlin
@_input
userName? Enter your name
userAge? Enter your age

@_output
- path? outputFolder/user_data.txt
- replaceExistingFile? false
Hi,
my name is {{userName}} and I'm {{userAge}} years old.
```