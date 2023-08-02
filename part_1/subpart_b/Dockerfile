FROM busybox

# Ajout de la valeur de la variable 2
ENV VAR_1="Some variable for 1"
ENV VAR_2="Some variable for 2"

# pas besoin de définir la valeur de la variable d'environnement dans l'export.
RUN export VAR_1
RUN export VAR_2

CMD echo FOO is $VAR_1, BAR is $VAR_2