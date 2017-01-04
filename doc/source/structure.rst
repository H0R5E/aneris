=======================================================
Description of Components for Module Integration in WP7
=======================================================

:Author: Mathew B. R. Topper
:Date:   17/09/2014

Data Hub
========

The data hub is a management tool that will facilitate data environments
without conflicts and flexible connections between various computational
models within the DTOcean project. The purpose of the Data Hub will be
to ensure that the requirements of each module can be fulfilled and that
a single set of homogenised variables are used (internally) so that
there are no semantic conflicts between modules. Additionally the Data
Hub will manage various "states" of the data, in order to distinguish
between data sources, be that static data (possibly accessed through a
database) or updated data from a previous run of the computational
module.

Note that the data hub is in no way intelligent, and shall be developed
independently from the optimisation program. The data hub is designed to
manage requests for data from various sources and then safely and
reliably retrieve that data for display or further processing.

Most importantly, the data hub must be extremely "resilient", possibly
designed using an "Asynchronous Component based Event Application
Framework", such as Python circuits. This creates both good fault
resistance and an ability to operate many requests in parallel,
something that could be key for reducing the time required for the
optimisation module.

Hub Interfaces
==============

The data hub interfaces are the primary tool for "attaching" a
computational or data catalog to the data hub. In some respects, the
computational models must also be considered data models, in the
abstract sense, to allow the easy use of surrogate models.

The interfaces for different classes of data catalog may differ
significantly from each other, and so these differences are discussed in
subsections below.

Module Interface
----------------

The module interface defines a clear set of input requirements for the
execution of the computational module and, following this, a definition
of the results that are produced. These results can then be made
available in the data hub's internal data catalog.

Although the module interface exists to provide a flexible system for
interacting with the computational models of the DTOcean project, it
would certainly be beneficial to align the inputs and outputs of the
various computational models so that the complexity of the module
interface is not too great at this stage.

Given the data hub will utilise the Python Pandas data analysis module,
outputs that are compatible with this module - either directly or
through file reading would be beneficial.

Additionally, inputs to the computational modules that are from a
distinct subset of well understood and highly Python compatible file
formats would be beneficial both to workpackage 7 and the DTOcean
project as a whole. Thus, the proposed list of such inputs types are:

-  Command line options
-  ODF Spreadsheets
-  ConfigObj configuration files
-  YAML files
-  Other Pandas compatible table formats

The module interface will be capable to executing the module after
checking all inputs are satisfied and will also check the condition of
the module during and after execution.

DataBase Interface
------------------

Given that the relationships in databases are generally complex, the
database interface requires a different approach to the computational
modules. It is anticipated that an Object Relational Model of the
existing DTOcean database will be produced using the Python SQLAlchemy
package. This will facilitate both easy access to the database (Python
Pandas can read SQL tables anyway) and the possibility to modify the
existing database structure with new results and variables.
Additionally, SQLAlchemy provides a level of flexibility for database
choice and thus the most appropriate system for the user can be chosen,
be that locally stored such as SQLite, or a server based solution.

Effective database operation may be extremely useful should the system
be employed using more powerful computational tool that are external to
the DTOcean system (i.e. any program for which a simple Python wrapper
can not be developed), as the state of the DTOcean variables must be
safely stored and recovered once the external tool has produced a result
and the system is ready to be restarted. Although Python has several
methods that could be utilised for this purpose (Python Pickle module),
the use of an external database could be also be beneficial for
monitoring the progress of the calculations and comparing previous
states.

Module User Interfaces
======================

In the light of the discussion of the module interface section, it is
proposed that each computational module is operable independently and
thus some user interface is required for each. Given that a graphical
tool will be produced as part of WP7, there appears to be no necessity
on a per module based.

It is proposed that the ideal solution is to develop a command line tool
for each computational module that uses the file specification discussed
above, i.e.

-  Command line options
-  ODF Spreadsheets
-  ConfigObj configuration files
-  YAML files
-  Other Pandas compatible table formats

Again, for ease of use, the most likely outputs are files with a Pandas
compatible format (csv files, spreadsheet files). Further complexity in
the inputs and outputs can be considered on a case by case basis as this
will impact upon the design of the module interface also.

Control Module
==============

The control module is the "intelligent" component of the system that
makes requests to the data hub. The requests will be some combination of
a data type, a source, and a state, to which the data hub will either
retrieve the data from it's own internal memory or from one of the
attached data catalog.

It is anticipated that the optimisation routines will form some part of
the control module, although this may be an independent component to
allow hassle free modification in the future.
