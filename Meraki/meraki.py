import meraki
#Need to verify authentication using an environment variable. Need to figure that out still
dashboard = meraki.DashboardAPI()
#save organization ID into variable for ease of use
organization_id = dashboard.organizations.getOrganizations()

#possibly do the same for network ID, where it is saved to a variable list/dictionary, but unsure if this will be unnecessary, or to much information to work with.
network_id =[]

