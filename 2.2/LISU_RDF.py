from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, OWL

g = Graph()

# Create an identifier to use as the subject for Donna.
donna = BNode()

# Add triples using store's add method.
g.add( (donna, RDF.type, OWL.device) )
g.add( (donna, OWL.nick, Literal("spacenavigator", lang='en')) )
g.add( (donna, OWL.name, Literal("USB\VID_046D")) )
g.add( (donna, OWL.vendor, Literal("PID_C626")) )
g.add( (donna, OWL.version, Literal("1.0")) )
g.add( (donna, OWL.device_type, Literal("HYBRID")) )
g.add( (donna, OWL.device_port, Literal("USB")) )
g.add( (donna, OWL.number_dof, Literal("6")) )

# Iterate over triples in store and print them out.
print("--- printing raw triples ---")
for s, p, o in g:
    print((s, p, o))

# For each foaf:Person in the store print out its mbox property.
print("--- printing mboxes ---")
for person in g.subjects(RDF.type, OWL.Person):
    for mbox in g.objects(person, OWL.mbox):
        print(mbox)

# Bind a few prefix, namespace pairs for more readable output
g.bind("dc", DC)
g.bind("owl", OWL)

print( g.serialize(format='pretty-xml') )
