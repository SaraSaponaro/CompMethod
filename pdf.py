
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline
from matplotlib import pyplot as plt
from scipy.stats import chisquare


class ProbabilityDensityFunction(InterpolatedUnivariateSpline):
    """Class describing a probability density function.
    """
    def __init__(self, x, y):  #la y non serve!!
        """Constructor."""
        InterpolatedUnivariateSpline.__init__(self, x, y)
        ycdf = [self.integral(0, xcdf) for xcdf in x]
        self.cdf = InterpolatedUnivariateSpline(x, ycdf)
        """controllo che siano unici"""
        x = np.unique(x)
        self.ppf = InterpolatedUnivariateSpline(ycdf, x)


    def prob(self, x1, x2):
        """Return the probability for the random variable to be included
        between x1 and x2."""
        return self.cdf(x2) - self.cdf(x1)

    def rnd(self, size):
        """Return an array of random values from the pdf.
        """
        return self.ppf(np.random.uniform(size=size))

    #def per controllare sline
    #[optional] how many random numbers do you have to throw to hit the/
    #/ numerical inaccuracy of your generator?



if __name__ == '__main__':
    '''
    #densità di probabilità triangolare
    x = np.linspace(0., 1., 100)
    y = 2. * x
    #densità prob exp
    x = np.linspace(0., 1., 100)
    y = 2*np.exp(-2*x)
    '''

    #densita prob gaussina
    x = np.linspace(-1.,1., 100)
    y = np.exp(-x**2/2)/np.sqrt(2*np.pi)
    #print (pdf(x))

    pdf = ProbabilityDensityFunction(x, y)

    plt.subplot(2,2,1)
    plt.title('pdf')
    plt.plot(x, pdf(x), '-')
    #plot della distribuzione:
    #plt.plot(x,y,'r.')
    plt.xlabel('x')
    plt.ylabel('pdf(x)')

    plt.subplot(2,2,2)
    plt.title('cdf')
    plt.plot(x, pdf.cdf(x))
    plt.xlabel('x')
    plt.ylabel('cdf(x)')

    plt.subplot(2,2,3)
    plt.title('ppf')
    plt.plot(x, pdf.ppf(x))
    plt.xlabel('x')
    plt.ylabel('ppf(x)')

    plt.subplot(2,2,4)
    plt.title('Sampling')
    rnd = pdf.rnd(1000000)
    print (rnd)
    n, bins, _ = plt.hist(rnd, bins=100, density=True)
    chi, p = chisquare(n, y)
    print('n_freq={}, chiq={}, pvalue={}'.format(len(n),chi,p))

    plt.show()
