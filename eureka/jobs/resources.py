"""Jobs Resource."""

# Django Import-Export
from import_export import resources

# Model
from eureka.jobs.models import Job

class JobResource(resources.ModelResource):
    """Job resource."""
    # def save_instance(self,instance, using_transactions = True, dry_run=False):
    #     name = self.__class__
    #     try:
    #         super(name,self).save_instance(instance,using_transactions,dry_run)
    #     except IntegrityError:
    #         pass
    class Meta:
        model = Job
