# Knowledge Bot

#### The idea is to create a bot that stores json files as tables, and then the aplication will create a relation between the tables with the use of prefixers or sufixers.

#### In other words, this bot will create a custom knowledge mapper per user, that will have a query system for fetching and showing the knowledge the user had entered

#### Prefixers/sufixes should be like: #InstanceName <- this will associate the current value to another table instance. name.general.json <- .general indicates to the bot the current table is a generalization, i.e. other tables could inherit their definition (this is not necessary, since the knowledge map should be customizable for the user's necessity)