from dlm.models.components.hiddenlayer import HiddenLayer
from dlm.models.components.logisticregression import LogisticRegression
import theano.tensor as T

class MLP(object):

	def __init__(self, rng, input, n_in, n_hidden, n_out):

		self.embLayer = LookupTableLayer(
			rng=rng,
			input=input,
			emb_dim=emb_dim,
		)
		
		self.hiddenLayer = HiddenLayer(
			rng=rng,
			input=self.embLayer.output,
			n_in=n_in,
			n_out=n_hidden,
			activation=T.tanh
		)

		self.logRegressionLayer = LogisticRegression(
			input=self.hiddenLayer.output,
			n_in=n_hidden,
			n_out=n_out
		)

		self.L1 = (
			abs(self.hiddenLayer.W).sum()
			+ abs(self.logRegressionLayer.W).sum()
		)

		self.L2_sqr = (
			(self.hiddenLayer.W ** 2).sum()
			+ (self.logRegressionLayer.W ** 2).sum()
		)

		self.negative_log_likelihood = (
			self.logRegressionLayer.negative_log_likelihood
		)

		self.errors = self.logRegressionLayer.errors

		self.params = self.hiddenLayer.params + self.logRegressionLayer.params
