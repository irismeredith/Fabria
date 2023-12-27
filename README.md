# About Fabria

Fabria is a project to apply new techniques in physics-informed machine learning to problems in design and industry, with the aim of building a tool 
that designers and engineers can use in their daily practice.

We're initially working on building products for use in room acoustics applications: it's a field close to my heart, and the physics is not too complicated. The initial goals
are to train a neural network that can both give impulse and frequency response data for a given room in real-time as the design is being modified, and to use the ability
of physics-informed neural networks to solve inverse problems along with minor constrained optimisation tools to generate designs for rooms on the basis of required parameters.

This is very much a work in progress, and I apologise for any infelicities this may contain. In particular, I know that the commenting in this project is
rather patchy. Please keep an eye on how the codebase grows and develops, and you'll see it improve markedly.

# Project architecture

The project is structured as follows: we have a backend containing the model training and server elements: this is written mostly in Flask, with some 
computationally intensive code written in C. The frontend is written mostly in Vue, using TresJS for 3D rendering and Vuetify for UI elements.

My inclination is to build an alternate frontend for monitoring the training and development of models: the use cases are different enough that this would be
worthwhile, and it'd be simple enough. Will update when it happens.

I've not thought too much about deployment or a database layer yet: I'll implement those when I need them. I'm a purist though, so I'll probably just go with Postgres.

# About the author

I'm Iris, and I have a tragic fascination with computational physics. I'm doing this mostly for fun, though heaven knows, if I could get this to pay
the bills, I definitely would. We'll see where it goes.
